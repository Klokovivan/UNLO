from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse('')

# 1. понять как пользоваться template и как передавать какие то значения
# 2. понять как работать со статикой statiс: css and картинки
# 3. закрепить то, как работает связка urld.py and views