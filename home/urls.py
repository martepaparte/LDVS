from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view()),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('welcome', views.WelcomeView.as_view(), name='welcome'),
    path('userlogout', views.LogoutInterfaceView.as_view(), name='userlogout'),
    path('', include('queryForm.urls'))
    # url(r'^logout/$', LogoutView.as_view(), name='logout')

]
