from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

#models 
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages 
from django.contrib.auth.models import User, Permission
from django.core.files.base import ContentFile
import datetime 

# Media Root
import os
from django.conf import settings
#root to where the images will be stored
mediaFile = settings.MEDIA_ROOT #os.path.join(settings.MEDIA_ROOT,'User_Profile')
#login required 
from django.contrib.auth.decorators import login_required
# packages
from . custom import deleteData
import time
from twilio.rest import Client
import yaml
#twilio account passsword and  key 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
import pdb

config = yaml.load(open(os.path.join(os.getcwd(),'config','con_file.yml')))
account_sid = config['twilio']['account_sid']
auth_token= config['twilio']['auth_token']
client = Client(account_sid, auth_token)


cameras = []
for idx in range(0, 20):
    cameras.append({
        'cid': f'cid - {idx}',
        'room': f'room - {idx}'
    })

# Create your views here.
@login_required(login_url='/login/')
@csrf_exempt
def home(request):
    cameras = Camera.objects.all()
    return render(request, 'dashboard/index.html', {
        'cameras' : cameras
    })

@login_required(login_url='/login/')
@csrf_exempt
def detected_images(request):
    cameras = Camera.objects.all()
    return render(request, 'dashboard/detected_images.html', {
        'cameras' : cameras
    })

@login_required(login_url='/login/')
@csrf_exempt
def fetch_images(request):
    cameras = Camera.objects.all()
    return render(request, 'dashboard/content.html', 
        {'cameras': cameras}
    )

# view to log_out 
def logout_request(request):
    logout(request)
    if 'next_url' in request.GET:
        next_url = request.GET['next_url']
        return redirect(next_url)
    else:
        messages.info(request,"Logged out successfully")
        return redirect('login')


def login_request(request):
    if request.user.is_authenticated:
        return redirect('health:home')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            print('Form is being Validated')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('health:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            print('Form is being Posted')
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login/index.html",
                    context={"form":form})
