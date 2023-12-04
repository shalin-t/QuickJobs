from django.views.generic import TemplateView,ListView

from employer.models import JobPosting
class HomePageView(ListView):
    model = JobPosting
    template_name='home.html'



