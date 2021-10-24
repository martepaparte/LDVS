from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginInterfaceView.as_view()),
    path('welcome', views.WelcomeView.as_view()),
]