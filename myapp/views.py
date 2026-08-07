from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def sayhello(request):
    return HttpResponse("Hello, world!")

def homework2(request, name):
    now = datetime.now()
    return render(request, 'show.html', locals())