#from django.contrib import admin
from django.urls import path, include
from .views import JobDetailView,JobCreateView,JobUpdateView,JobDeleteView,CandidatesView

urlpatterns = [
    path("new/", JobCreateView.as_view(), name="job_new"), # new
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"), # new
    path("<int:pk>/edit/", JobUpdateView.as_view(), name="job_edit"), # new
    #path("", JobListView.as_view(), name="home"),
    path("<int:pk>/delete/", JobDeleteView.as_view(),name="job_delete"),
    path("candidates/", CandidatesView.as_view(), name="candidate"), # new
]