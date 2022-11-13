from django.urls import path, include

from . import views

urlpatterns = [
    path('order/new', views.CreateOrderFormView.as_view(), name="order.new")
]