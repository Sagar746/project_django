from django.shortcuts import render,reverse,redirect
from django.contrib.auth.views import LoginView

from django.views.generic import CreateView
from .forms import SignupForm
# Create your views here.

class CustomLogin(LoginView):
	template_name= 'login.html'

	def get_success_url(self):
		return reverse('app:home')

class SignupView(CreateView):
	template_name='signup.html'
	form_class = SignupForm

	def form_valid(self,form):
		form.save()
		return redirect('app:home')