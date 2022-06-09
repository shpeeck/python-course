from django.urls import path
from .views import hellodjango, name, date, year, day, month

urlpatterns = [
    path('', hellodjango),
    path('date/', date),
    path('date/year/', year),
    path('date/day/', day),
    path('date/month/', month),
    path('<str:name>/', name)
    
]