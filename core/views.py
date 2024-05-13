import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from base64 import b64encode
# Create your views here.
def index(request): 
    return render(request, 'index.html')
@login_required
def accounts(request): 
    if request.method== "POST":
        print(request.POST.get('login'))
        _=f"{request.POST.get('login')}:{request.POST.get('password')}"
        print(_)
        login_pass= b64encode(_.encode("utf-8")).decode("utf-8")
        print(login_pass)
        response= requests.post(
            "https://api.moysklad.ru/api/remap/1.2/security/token",
            headers= {
                "Authorization": f"Basic {login_pass}",
                "Accept-Encoding": "gzip"
            })
        print(response.status_code)
    return render(request, 'accounts.html')

@login_required
def meow(request): 
    return render(request, 'meow.html', {
        'items': [
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
            {
                'name': 'sl,al,;,sa;lld,dlf',
                'size': '2mb',
                'date': '24.04.2024'
            },
        ]
    })



#HttpResponse('')

# 1. 
# 2.
# 3. 