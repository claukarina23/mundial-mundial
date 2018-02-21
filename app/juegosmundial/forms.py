from django import forms

from app.juegosmundial.models import Equipo

class EquipoForm(forms.ModelForm):

	class Meta:
		model = Equipo

#tupla
		fields = [
			'tactica',
			'jugadores',
			'usuario',
		]

		labels = {
			'tactica': 'Tactica',
			'jugadores': 'Jugadores',
			'usuario': 'Usuario',
		}
		widgets = {
			'tactica' : forms.TextInput(attrs={'class':'form-control'}),			
			'jugadores': forms.CheckboxSelectMultiple(),
			'usuario' : forms.Select(attrs={'class':'form-control'}),
		}