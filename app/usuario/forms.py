from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#agregando
from django.contrib.auth import (authenticate,get_user_model,login,logout)
from django import forms

User = get_user_model()

class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
    	username = self.cleaned_data.get("username")
    	password = self.cleaned_data.get("password")
    	user = authenticate(username=username, password=password)
    	if not user:
    		raise forms.ValidationError("Usuario y/o Contraseña incorrecta")
    	if not user.check_password(password):
	    	raise forms.ValidationError("Incorrecto password")
    	return super(UserLoginForm, self).clean(*args, **kwargs)