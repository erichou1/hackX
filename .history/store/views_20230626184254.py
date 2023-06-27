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
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
    return render(request, 'store/404.html')

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
        html = """\
<div style="height:100%;margin:0;font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;background-color:#f2f4f6;color:#51545e;width:100%!important">
    <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;margin:0;padding:0;background-color:#f2f4f6">
      <tbody><tr>
        <td align="center" style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px">
          <table width="100%" cellpadding="0" cellspacing="0" role="presentation" style="width:100%;margin:0;padding:0">
            <tbody><tr>
              <td style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px;padding:25px 0;text-align:center">
                <a href="https://www.losgatoshacks.com" style="color:#a8aaaf;font-size:16px;font-weight:bold;text-decoration:none" target="_blank">
                  <img src="https://i.imgur.com/2ahJi9R.png" width="90" height="90" border="0" style="border:none;width:94px" class="CToWUd" data-bit="iit">
              </a>
              </td>
            </tr>
            
            <tr>
              <td width="570" cellpadding="0" cellspacing="0" style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px;width:100%;margin:0;padding:0">
                <table align="center" width="570" cellpadding="0" cellspacing="0" role="presentation" style="width:570px;margin:0 auto;padding:0;background-color:#ffffff">
                  
                  <tbody><tr>
                    <td style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px;padding:45px">
                      <div>
                        <h1 style="margin-top:0;color:#333333;font-size:22px;font-weight:bold;text-align:left">Hi """+content['student_name']+""",</h1>
<p style="margin:0.4em 0 1.1875em;font-size:16px;line-height:1.625;color:#51545e">Congratulations! You have succesfully registered for the 2023 Los Gatos Hacks Hackathon on 9/9-9/10. We can't wait to see what amazing creations you can bring to life! <br><br>
  Use the button below to find all of the information you will need to know prior to the hackathon including  the date, location, and what you will need to bring!
<table align="center" width="100%" cellpadding="0" cellspacing="0" style="width:100%;margin:30px auto;padding:0;text-align:center">
  <tbody><tr>
    <td align="center" style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px">
      
      <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tbody><tr>
          <td align="center" style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px">
            <table border="0" cellspacing="0" cellpadding="0">
              <tbody><tr>
                <td style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px">
                  <a href="https://docs.google.com/document/d/1AxMnJsCBffj9N33eq0h_nOUySqrZfXEBEC9V_4L2EkY/edit?usp=sharing" style="color:#ffffff;background-color:#000000;border-top:10px solid #000000;border-right:18px solid #000000;border-bottom:10px solid #000000;border-left:18px solid #000000;display:inline-block;text-decoration:none;border-radius:3px;box-sizing:border-box" target="_blank" data-saferedirecturl="https://docs.google.com/document/d/1AxMnJsCBffj9N33eq0h_nOUySqrZfXEBEC9V_4L2EkY/edit?usp=sharing">Information</a>
                </td>
              </tr>
            </tbody></table>
          </td>
        </tr>
      </tbody></table>
    </td>
  </tr>
</tbody></table>
<p style="margin:0.4em 0 1.1875em;font-size:16px;line-height:1.625;color:#51545e">If you have any further questions contact us at <a href="mailto:support@losgatoshacks.com" style="color:#3869d4" target="_blank">support@losgatoshacks.com</a></p>
<p style="margin:0.4em 0 1.1875em;font-size:16px;line-height:1.625;color:#51545e">Kind regards,
  <br>Los Gatos Hacks Team</p>

                      </div>
                    </td>
                  </tr>
                </tbody></table>
              </td>
            </tr>
            <tr>
              <td style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px">
                <table align="center" width="570" cellpadding="0" cellspacing="0" role="presentation" style="width:570px;margin:0 auto;padding:0;text-align:center">
                  <tbody><tr>
                    <td align="center" style="font-family:&quot;Nunito Sans&quot;,Helvetica,Arial,sans-serif;font-size:16px;padding:45px">
                      <p style="margin:0.4em 0 1.1875em;font-size:13px;line-height:1.625;color:#a8aaaf;text-align:center">© 2023 Los Gatos Hacks. All rights reserved.</p>
                    </td>
                  </tr>
                </tbody></table>
              </td>
            </tr>
          </tbody></table>
        </td>
      </tr>
    </tbody></table>

        """
        msg = MIMEMultipart('alternative')  
        msg['Subject'] = "Los Gatos Hacks Registration Confirmation"
        msg.attach(MIMEText(html, 'html'))

        with smtplib.SMTP_SSL('smtp.mail.us-east-1.awsapps.com', 465) as connection:
            email_address = 'support@losgatoshacks.com'
            email_password = 'Stopguessing1567'
            connection.login(email_address, email_password)
            connection.sendmail(from_addr=email_address, to_addrs=content['student_email'],
                        msg=msg.as_string())

    except:
        pass
    return HttpResponse(request.POST.get("data"))
