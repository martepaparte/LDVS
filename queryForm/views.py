from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, ListView, DetailView

from .forms import RequestQueryForm

from .models import RequestQuery


class FormCreateView(CreateView):
    model = RequestQuery
    success_url = '/'
    form_class = RequestQueryForm


class RequestQueryListView(ListView):
    model = RequestQuery
    context_object_name = 'request_queries'
    template_name = 'queryForm/queryforms_list.html'


class RequestQueryDetailsView(DetailView):
    model = RequestQuery
    context_object_name = 'request_query'
    template_name = 'queryForm/queryforms_detail.html'
