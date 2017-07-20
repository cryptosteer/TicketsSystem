from django.shortcuts import render
from .models import Serie, Ticket
from .serializers import SerieSerializer, TicketSerializer
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class SerieViewSet(ModelViewSet):

    queryset = Serie.objects.all()
    serializer_class = SerieSerializer


class TicketViewSet(ModelViewSet):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


@csrf_exempt
def serie_list(request):
    if request.method == 'GET':
        series = Serie.objects.all()
        serializer = SerieSerializer(series, many=True)
        return JSONResponse(serializer.data)
