from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, TemplateView

from .forms import QueryForm

from .models import RequestQuery


class FormCreateView(CreateView):
    model = RequestQuery
    success_url = '/'
    form_class = QueryForm
