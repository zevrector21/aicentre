from django.contrib import admin
from .models import *
from . custom import deleteData
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import pdb
from django.utils.html import format_html

#Change header 

admin.site.site_header = "AI Management Dashboard"

class CameraAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<a href="/media/LabelImages/{ obj.labled_image }" target="blank"><img src="/media/LabelImages/{ obj.labled_image }" width="100" /></a>')

    list_display = ['cid', 'title', 'room', 'resident', 'description', 'medical_condition', 'image']
    search_fields = ['cid', 'title', 'room']

admin.site.register(Camera, CameraAdmin)

class ArchivedImageAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<a href="/media/LabelImages/{ obj.name }" target="blank"><img src="/media/LabelImages/{ obj.name }" width="100" /></a>')

    list_display = ['camera', 'status', 'created_at', 'image']
    list_filter = ['status']
    search_fields = ['camera', 'status']


admin.site.register(ArchivedImage, ArchivedImageAdmin)

class DetectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'status']
    search_fields = ['code', 'description']
    
admin.site.register(Detection, DetectionAdmin)

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'description']
    search_fields = ['name', 'number']
    
admin.site.register(PhoneNumber, PhoneNumberAdmin)
