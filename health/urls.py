from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views

app_name="health"

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_images/',views.fetch_images, name='fetch_images'),
    path('archived-events/',views.archived_events, name='archived_events'),
]
