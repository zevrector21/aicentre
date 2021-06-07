from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Camera(models.Model):
    cid = models.CharField(max_length=100, blank=False, unique=True)
    title = models.CharField(max_length=100, blank=False)
    room = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, blank=True)
    medical_condition = models.CharField(max_length=255, blank=True)
    labled_image = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Detection(models.Model):
    code = models.CharField(max_length=20, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False)
    enable = models.BooleanField(blank=True, default=False)

    def __str__(self):
        return self.description

class ArchivedImage(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, blank=False)
    name = models.CharField(max_length=100, blank=False)
    status = models.ForeignKey(Detection, on_delete=models.PROTECT, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    number = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
    schedule = models.CharField(max_length=100, blank=True)
    enable = models.BooleanField(blank=True, default=True)    
    
    def __str__(self):
        return self.number

class Resident(models.Model):
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, blank=False)
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, blank=True)
    face_picture = models.ImageField(upload_to='user_profile')
    body_picture = models.ImageField(upload_to='user_profile')
    side_picture = models.ImageField(upload_to='user_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True, default=True)

    def __str__(self):
        return self.name
