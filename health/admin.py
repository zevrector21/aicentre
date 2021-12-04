from django.contrib import admin
from .models import *
from . custom import deleteData
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
import pdb
from django.utils.html import format_html

#Change header 

admin.site.site_header = " "

class CameraAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<a href="/media/LabelImages/{ obj.labled_image }" target="blank"><img src="/media/LabelImages/{ obj.labled_image }" width="100" /></a>')

    def latest_updated_at(self, obj):
    	return obj.updated_at.strftime('%b %d, %Y, %H:%M:%S')

    list_display = ['cid', 'title', 'room', 'description', 'medical_condition', 'latest_updated_at', 'image']
    search_fields = ['cid', 'title', 'room']

admin.site.register(Camera, CameraAdmin)

class ArchivedEventAdmin(admin.ModelAdmin):
    def image(self, obj):
        return format_html(f'<a href="/media/ArchiveEvents/{ obj.name }" target="blank"><img src="/media/ArchiveEvents/{ obj.name }" width="100" /></a>')

    def latest_updated_at(self, obj):
    	return obj.updated_at.strftime('%b %d, %Y, %H:%M:%S')

    list_display = ['name', 'camera', 'status', 'latest_updated_at', 'image']
    list_filter = ['status']
    search_fields = ['camera', 'status']

admin.site.register(ArchivedEvent, ArchivedEventAdmin)

class DetectionAdmin(admin.ModelAdmin):
    list_display = ['code', 'description', 'enable']
    search_fields = ['code', 'description']
    
admin.site.register(Detection, DetectionAdmin)

class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'description', 'schedule', 'enable']
    search_fields = ['name', 'number']
    
admin.site.register(PhoneNumber, PhoneNumberAdmin)

class ResidentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'camera', 'face_picture', 'body_picture', 'side_picture', 'status']
    search_fields = ['name', 'number']
    
admin.site.register(Resident, ResidentAdmin)

class ReplyTypeAdmin(admin.ModelAdmin):
    list_display = ['number', 'description']
    
admin.site.register(ReplyType, ReplyTypeAdmin)

class NotificationRuleAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'camera', 'reply_type', 'created_at', 'updated_at']
    
admin.site.register(NotificationRule, NotificationRuleAdmin)
