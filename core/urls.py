from django.urls import path
from django.contrib.auth import views as auth_views

from . import views  



urlpatterns = [
    path('', views.index, name='index'),
    #path('abc', views.abc, name='abc'),
    path('accounts/', views.accounts, name='accounts'),
    path('meow/', views.meow, name='meow'),
    #path('abc/', views.abc, name='abs'),
    
]

