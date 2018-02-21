from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

#agregando
from django.contrib.auth import (authenticate,get_user_model,login,logout)

from app.usuario.forms import RegistroForm,UserLoginForm

# Create your views here.

class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')

def login_view(request):
	print("entro a funcidon login")
	title = "Login"
	form = UserLoginForm(request.POST or None)
	username = None
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		print("entro")
		return render(request,"usuario/bienvenido.html", {"form":form,
														  "title":title,
														  "username":username})
	print(title)
	print(form)
	return render(request,"form.html", {
		"form":form, 
		"title":title,
		"username":username})

def register_view(request):
	return render(reques,"form.html", {})

def logout_view(request):
	return render(reques,"form.html", {})

