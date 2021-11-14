from django.shortcuts import render
from django.views.generic import CreateView
from .models import Order
from .forms import CreateOrderForm


class CreateOrderFormView(CreateView):
    model = Order
    success_url = '/'
    form_class = CreateOrderForm

