from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('query/new', views.FormCreateView.as_view(), name="query.new"),
]
