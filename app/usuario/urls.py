from django.conf.urls import url
from app.usuario.views import RegistroUsuario

app_name = 'usuario'

urlpatterns = [
	url(r'^registrar', RegistroUsuario.as_view(), name='registrar'),

]