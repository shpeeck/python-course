"""drfProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from firstApp import views
from firstApp.urls import router as store_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('today/', views.today),
    path('hello_world/', views.hello_world),
    path('my_name/', views.my_name),
    path('calculator/', views.calculator),
    path('stores-old/', views.StoreApiView.as_view()),
    path('', include(store_router.urls)),
]
