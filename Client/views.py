from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def customer(request):
    context = {}
    return render(request, 'Client/customer.html', context)


def agent(request):
    context = {}
    return render(request, 'Client/agent.html', context)
