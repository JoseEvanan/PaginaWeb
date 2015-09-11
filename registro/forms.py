from django.forms import ModelForm
from .models import Registro
from .models import Cita


class CitaForm(ModelForm):
	class meta:
		print "meta!!"
		model=Cita
		print "model!!"
		fields=('nomb','busca','registros',)
		print fields
		print "fields"

class RegistroForm(ModelForm):
	class Meta:
		model = Registro
		fields = ('nombres', 'apellido_paterno','apellido_materno','dni','telefono','correo','tipo_persona',)


