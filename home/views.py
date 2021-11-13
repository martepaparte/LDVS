import time

from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class WelcomeView(TemplateView):
    template_name = 'home/user_logged_in.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class MainPageView(TemplateView):
    template_name = 'home/main.html'
