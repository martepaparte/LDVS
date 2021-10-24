from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('welcome', views.WelcomeView.as_view(), name='welcome'),
    path('userlogout', views.LogoutInterfaceView.as_view(), name='userlogout'),
    # url(r'^logout/$', LogoutView.as_view(), name='logout')

]
