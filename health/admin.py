from django.contrib import admin
from .models import *
from . custom import deleteData
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import pdb

#Change header 

admin.site.site_header = "AI Management Centre"

class CameraAdmin(admin.ModelAdmin):
    list_display = ['cid', 'title', 'room', 'resident', 'description', 'medical_condition', 'labled_image']
    list_filter = ['cid', 'title', 'room']
    search_fields = ['title', 'room']

admin.site.register(Camera, CameraAdmin)

class ArchivedImageAdmin(admin.ModelAdmin):
    list_display = ['camera', 'name', 'status', 'created_at', 'updated_at']
    list_filter = ['camera', 'name', 'status']
    search_fields = ['camera', 'status']
    
admin.site.register(ArchivedImage, ArchivedImageAdmin)

class DetectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'description']
    list_filter = ['code', 'description']
    search_fields = ['code', 'description']
    
admin.site.register(Detection, DetectionAdmin)
