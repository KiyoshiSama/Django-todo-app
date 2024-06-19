from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView,CreateView
from .forms import UserRegisterForm

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserRegisterForm
    success_url = '/accounts/login/'
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    
class CustomLoginView(LoginView):
    fields = "username","password"
    next = "/"
       
class LogoutView(LogoutView):
    next_page = '/accounts/login'

    
