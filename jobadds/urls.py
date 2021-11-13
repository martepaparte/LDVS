from django.urls import path, include

from . import views

urlpatterns = [
    path('add/new', views.JobAddCreateView.as_view(), name="add.new.job"),
    path('jobs', views.JobsView.as_view(), name="see.all.jobs"),
    path('jobs/<int:pk>', views.JobDetailsView.as_view(), name="job.details")

]
