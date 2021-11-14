from django.shortcuts import render
from django.views.generic import ListView, DetailView
from home.models import MyUser


class ClientListView(ListView):
    model = MyUser.CLIENT
    context_object_name = 'clients'
    template_name = 'customUserManager/clients/client_list.html'


class ClientDetailView(DetailView):
    model = MyUser.CLIENT
    context_object_name = 'client'
    template_name = 'customUserManager/clients/client_detail.html'


