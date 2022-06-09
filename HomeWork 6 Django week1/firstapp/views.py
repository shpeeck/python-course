from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import datetime

now = datetime.datetime.now()

# Create your views here.
myDate = "(22.03.2022)"

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")
    
def name(request, name):
    return HttpResponse(f"Hello {name}!")
    
def date(request):
    return HttpResponse(now.strftime("%d.%m.%Y"))
    
def year(request):
    return HttpResponse(now.strftime("%Y"))
    
def day(request):
    return HttpResponse(now.strftime("%d"))
    
def month(request):
    return HttpResponse(now.strftime("%m"))