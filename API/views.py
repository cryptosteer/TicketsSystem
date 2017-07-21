from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.contrib.humanize.templatetags.humanize import naturalday
from django.template.defaultfilters import linebreaksbr
from django.db.models import Q
import datetime
from .models import Ticket, TicketItem, TicketProblem, TicketPriority, TicketStatus
from .serializers import TicketSerializer, TicketListSerializer, \
    TicketPrioritySerializer, TicketProblemSerializer, TicketItemSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class TicketViewSet(ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketProblemViewSet(ModelViewSet):

    queryset = TicketProblem.objects.all()
    serializer_class = TicketProblemSerializer


class TicketPriorityViewSet(ModelViewSet):

    queryset = TicketPriority.objects.all()
    serializer_class = TicketPrioritySerializer


@csrf_exempt
def ticket_list(request):
    if request.method == 'POST':
        data = []
        queryset = Ticket.objects.filter(Q(created_by=request.user))
        for item in queryset:
            data.append(TicketItem(
                item.id, item.order_number, naturalday(item.created_date), '', '', item.priority.name,
                item.problem.name, '', item.status.name, item.assigned_to))
        serializer = TicketListSerializer(data, many=True)
        return JSONResponse(serializer.data)
    else:
        return HttpResponse('Ok')


@csrf_exempt
def pending_ticket_list(request):
    if request.method == 'POST':
        data = []
        open_status = TicketStatus.objects.get(value="open")
        replied_status = TicketStatus.objects.get(value="clientreply")
        queryset = Ticket.objects.filter(
            Q(status=open_status) | (Q(status=replied_status) & Q(assigned_to=request.user)))
        for item in queryset:
            data.append(TicketItem(
                item.id, item.order_number, naturalday(item.created_date), '', '',
                item.priority.name, item.problem.name, '', item.status.name,
                item.assigned_to))
        serializer = TicketListSerializer(data, many=True)
        return JSONResponse(serializer.data)
    else:
        return HttpResponse('Ok')


@csrf_exempt
def closed_ticket_list(request):
    if request.method == 'POST':
        data = []
        closed_status = TicketStatus.objects.get(value="closed")
        filterargs = {'status': closed_status}
        queryset = Ticket.objects.filter(**filterargs)
        for item in queryset:
            data.append(TicketItem(
                item.id, item.order_number, naturalday(item.created_date), '', '', item.priority.name,
                item.problem.name, '', item.status.name, item.assigned_to))
        serializer = TicketListSerializer(data, many=True)
        return JSONResponse(serializer.data)
    else:
        return HttpResponse('Ok')


@csrf_exempt
def ticket_create(request):
    if request.method == 'POST':
        priority = TicketPriority.objects.get(pk=request.POST['priority'])
        problem = TicketProblem.objects.get(pk=request.POST['problem'])
        ticket = Ticket(
            order_number=request.POST['order_number'], priority=priority,
            problem=problem, description=request.POST['description'],
            created_by=request.user)
        ticket.save()
        return HttpResponse('Ok')


@csrf_exempt
def get_ticket(request):
    if request.method == 'POST':
        item = Ticket.objects.get(pk=request.POST['id'])
        closed_date = item.closed_date.strftime("%d/%m/%Y") if item.closed_date is not None else ''
        ticket = TicketItem(
            item.id, item.order_number, item.created_date.strftime("%d/%m/%Y"), closed_date,
            item.created_by, item.priority.name, item.problem.name,
            linebreaksbr(item.description), item.status.name, item.assigned_to)
        serializer = TicketItemSerializer(ticket)
        return JSONResponse(serializer.data)


@csrf_exempt
def reply_ticket(request):
    if request.method == 'POST':
        ticket = Ticket.objects.get(pk=request.POST['id'])
        ticket.description += '\n\n' + '--REPLY--' + '\n\n' + request.POST['reply']
        ticket.status = TicketStatus.objects.get(value='clientreply')
        ticket.save()
        return HttpResponse('Ok')


@csrf_exempt
def answer_ticket(request):
    if request.method == 'POST':
        ticket = Ticket.objects.get(pk=request.POST['id'])
        ticket.description += '\n\n' + '--ANSWER--' + '\n\n' + request.POST['answer']
        ticket.assigned_to = request.user
        ticket.status = TicketStatus.objects.get(value='answered')
        ticket.save()
        return HttpResponse('Ok')


@csrf_exempt
def close_ticket(request):
    if request.method == 'POST':
        ticket = Ticket.objects.get(pk=request.POST['id'])
        ticket.description += '\n\n' + '--CLOSED--' + '\n\n' + request.POST['answer']
        ticket.status = TicketStatus.objects.get(value='closed')
        ticket.closed_date = datetime.datetime.now()
        ticket.assigned_to = request.user
        ticket.save()
        return HttpResponse('Ok')
