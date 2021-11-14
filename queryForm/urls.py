from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('query/new', views.FormCreateView.as_view(), name="query.new"),
    path('query/list', views.RequestQueryListView.as_view(), name="see.all.request.queries"),
    path('query/list/<int:pk>', views.RequestQueryDetailsView.as_view(), name="request.query.details")

]
