from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from . import views

app_name="health"

urlpatterns = [
    path('', views.home, name='home'),
    path('fetch_images/',views.fetch_images, name='fetch_images'),
    path('archived_images/',views.archived_images, name='archived_images'),
]
