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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
def archived_images(request):
    today = str(datetime.date.today())
    start_date = request.GET.get('start_date', '1983-01-01')
    end_date = request.GET.get('end_date', '2100-01-01')
    camera = int(request.GET.get('camera', -1))
    status = int(request.GET.get('status', -1))
    cameras = Camera.objects.all()
    detections = Detection.objects.all()

    if camera == -1 and status == -1:
        archived_images = ArchivedImage.objects.filter(
            created_at__range=[start_date, end_date],
        ).order_by('-created_at')
    else:
        archived_images = ArchivedImage.objects.filter(
            created_at__range=[start_date, end_date],
            status=status,
            camera=camera
        ).order_by('-created_at')
        if status == -1:
            archived_images = ArchivedImage.objects.filter(
                created_at__range=[start_date, end_date],
                camera=camera,
            ).order_by('-created_at')
        if camera == -1:
            archived_images = ArchivedImage.objects.filter(
                created_at__range=[start_date, end_date],
                status=status
            ).order_by('-created_at')
    
    page = request.GET.get('page', 1)
    paginator = Paginator(archived_images, 10)

    try:
        form = paginator.page(page)
    except PageNotAnInteger:
        form = paginator.page(1)
    except EmptyPage:
        form = paginator.page(paginator.num_pages)

    query_set = request.META.get('QUERY_STRING', '')
    if '&page' in query_set:
        query_set = query_set.split('&page')[0]

    return render(request, 'dashboard/archived_images.html', {
        'start_date': start_date,
        'end_date': end_date,
        'camera': camera,
        'status': status,
        'form':form,
        'query_set': query_set,
        'cameras': cameras,
        'detections': detections
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
