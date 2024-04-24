from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return render(request, 'index.html')


def abc(request): 
    
    return render(request, 'abc.html')


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

# 1. понять как пользоваться template и как передавать какие то значения
# 2. понять как работать со статикой statiс: css and картинки
# 3. закрепить то, как работает связка urld.py and views