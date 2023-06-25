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
import smtplib 
import gspread
# Create your views here.
from .models import *

sa = gspread.service_account(filename="services_account.json")
sh = sa.open("Los Gatos Hacks Emails")
wks = sh.worksheet("Registrations")
def store(request):
    context = {}
    return render(request, 'store/main.html')
def error_404 (request, exception):
    retun render(request)
def email(request):
    context = {}
    return render(request, 'store/email.html')

def sponsors(request):
    context = {}
    return render(request, 'store/sponsors.html')

def form(request):
    context = {}
    return render(request, 'store/form.html')
@csrf_exempt    
def myajaxtestview(request):
    
    # sh.add_worksheet(title="Registrations", rows=1, cols=9)
    
    content = eval(request.POST.get("data"))
    # print(content.keys())
    wks.append_row(list(content.values()))    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:  
            email_address = 'losgatoshacks@gmail.com'
            email_password = 'cnqlkhzkqsmiywnu'
            connection.login(email_address, email_password )
            connection.sendmail(from_addr=email_address, to_addrs=content['student_email'], 
            msg="subject:Los Gatos Hacks Registration Confirmation \n\n    Thanks for registering for the 2023 Los Gatos Hacks Hackathon on 9/9-9/10. We can't wait to see what amazing creations you can bring to life! \n    If you have any questions, please email us at losgatoshacks@gmail.com. \n\nKind regards, \nLos Gatos Hacks Team")
    except:
        pass
    return HttpResponse(request.POST.get("data"))
