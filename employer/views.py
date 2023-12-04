from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from employer.models import JobPosting
from accounts.models import CustomUser
# Create your views here.

class JobDetailView(DetailView):
    model = JobPosting
    template_name='jobdetails.html'

class JobCreateView(CreateView): # new
    model = JobPosting
    template_name = "jobcreate.html"
    fields = ["job_title", "job_description", "start_Date", "end_Date", "salary", "location"]

class JobUpdateView(UpdateView): # new
    model = JobPosting
    template_name = "jobupdate.html"
    fields = ["job_title", "job_description", "start_Date", "end_Date", "salary", "location"]

class JobDeleteView(DeleteView): # new
    model = JobPosting
    template_name = "jobdelete.html"
    success_url = reverse_lazy("home")

class CandidatesView(ListView): # new
    model = CustomUser
    template_name = "candidates.html"
   # success_url = reverse_lazy("home")

