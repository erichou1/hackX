from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import update_session_auth_hash

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
from .models import *


def store(request):
    context = {}
    return render(request, 'store/main.html')


def sponsors(request):
    context = {}
    return render(request, 'store/sponsors.html')

def form(request):
    context = {}
    return render(request, 'store/form.html')
@csrf_exempt    
def myajaxtestview(request):
    
    content = eval(request.POST['text'])
    print(content)
    import smtplib 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
        email_address = 'hackxhackathon@gmail.com'
        email_password = 'cvzolwemcagnqgol'
        connection.login(email_address, email_password )
        connection.sendmail(from_addr=email_address, to_addrs=content['student_email'], 
        msg="subject:hi \n\n this is my message")

    return HttpResponse(request.POST['text'])
