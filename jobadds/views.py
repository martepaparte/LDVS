from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages

from .forms import JobAddForm

from .models import JobAdd


class JobAddCreateView(CreateView):
    model = JobAdd
    success_url = '/'
    form_class = JobAddForm

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Forma sukurta sėkmingai.')
        form.clean()
        return HttpResponseRedirect(self.request.path_info)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.INFO, form.errors)
        return render(self.request, 'jobadds/jobadd_form.html', context={'form': form})


class JobsView(ListView):
    model = JobAdd
    context_object_name = 'jobs'
    template_name = 'jobadds/jobadds_list.html'


class JobDetailsView(DetailView):
    model = JobAdd
    context_object_name = 'job'
    template_name = 'jobadds/job_details.html'
