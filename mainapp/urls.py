# mainapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('control-led/', views.control_led, name='control_led'),
]