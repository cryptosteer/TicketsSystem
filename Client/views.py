from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


@login_required
def index(request):
    context = {}
    return render(request, 'Client/index.html', context)
