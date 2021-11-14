from django.urls import path, include

from . import views

urlpatterns = [
    path('client/list', views.ClientListView.as_view(), name="client.list"),
    path('client/list/<int:pk>', views.ClientDetailView.as_view(), name="client.detail"),

]