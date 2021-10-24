from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class WelcomeView(TemplateView):
    template_name = 'home/welcome.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


