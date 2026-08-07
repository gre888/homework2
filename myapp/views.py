from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def sayhello(request):
    now = datetime.now()
    print(now)
    return HttpResponse("Hello, world!")

def homework2(request, name):
    now = datetime.now()
    print(now)
    print(name)
    return render(request, 'show.html', locals())

import random
def lotto1(request):
    L1=random.sample(range(1, 10), 5)
    print(L1)
    return render(request, "lotto1.html", locals())
import random
def lotto2(request):
    L2=random.sample(range(1, 42), 6)
    L3=random.sample(range(1, 42), 6)
    L4=random.sample(range(1, 42), 6)
    L5=random.sample(range(1, 42), 6)
    L6=random.sample(range(1, 42), 6)
    L7=random.sample(range(1, 42), 6)
    lo=[L2,L3,L4,L5,L6,L7]
    print(lo)
    return render(request, "lotto2.html", locals())  
  
# import random
# def lotto1(request):
#     lotto1=random.sample(range(1, 10), 5)
#     print(lotto1)
#     # return HttpResponse("Hello dice1")
#     # return render(request, "dice1.html", locals())
#     return render(request, "lotto1.html", locals())