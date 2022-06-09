from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
myDate = "(22.03.2022)"

def hellodjango(request: HttpRequest):
    return HttpResponse("Hello Django!")
    
def name(request, name):
    return HttpResponse(f"Hello {name}!")
    
def date(request):
    return HttpResponse(myDate)
    
def year(request):
    return HttpResponse(myDate[7:11])
    
def day(request):
    return HttpResponse(myDate[1:3])
    
def month(request):
    return HttpResponse(myDate[4:6])