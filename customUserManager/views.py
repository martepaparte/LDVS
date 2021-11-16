from django.shortcuts import render
from django.views.generic import ListView, DetailView
from home.models import MyUser
from django.core import serializers


class ClientListView(ListView):
    model = MyUser
    context_object_name = 'clients'
    template_name = 'customUserManager/clients/client_list.html'

    def get_queryset(self):
        return MyUser.objects.filter(role=self.model.CLIENT)


class ClientDetailView(DetailView):
    model = MyUser
    context_object_name = 'client'
    data = serializers.serialize("python", MyUser.objects.all())
    template_name = 'customUserManager/clients/client_detail.html'


