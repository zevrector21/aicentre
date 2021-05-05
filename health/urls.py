from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views

app_name="health"

urlpatterns = [
    path('', views.main, name='main'),
    path('fetch_images/',views.fetch_images, name='fetch_images'),
]
