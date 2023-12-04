# accounts/urls.py
from django.urls import path
from .views import SignUpView,EmployerSignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("employer/signup", EmployerSignUpView.as_view(),name="empsignup"),
]