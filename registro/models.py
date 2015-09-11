from django.db import models
from django.utils import timezone
from django import forms
from django.forms import ModelForm
from django.forms import Form
USER_CHOICE= (
	('T','Trabajador'),
	('V','Visitante'),
	)

class Registro(models.Model):
	#score = models.IntegerField(choices=SCORE_CHOICES, blank=True)
	nombres = models.CharField(max_length=50)
	apellido_paterno = models.CharField(max_length=50)
	apellido_materno = models.CharField(max_length=50)
	dni = models.IntegerField()
	telefono = models.IntegerField()
	correo = models.EmailField()
	tipo_persona = models.CharField(max_length=15,choices=USER_CHOICE )

	def __unicode__(self):
		return self.nombres

class Cita(models.Model):
	registros = models.ForeignKey(Registro)
	buscar = models.CharField(max_length=50)

	def __unicode__(self):
		return self.buscar


class CitaForm(Form):
	if Registro.objects.all().count()>0 :
		nombres = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'  }))
		apellido_paterno = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
		apellido_materno = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'readonly':'readonly'}))
		buscar = forms.ModelChoiceField(queryset=Registro.objects.filter(tipo_persona='T').order_by('nombres'),widget=forms.Select(attrs={'onchange': 'activarBoton()'}))


class RegistroForm(ModelForm):
	class Meta:
		model = Registro
		fields = ('nombres', 'apellido_paterno','apellido_materno','dni','telefono','correo','tipo_persona',)
		widgets = {'tipo_persona': forms.Select(attrs={'onchange': 'activarBoton()'}),
					'nombres': forms.TextInput(attrs={'placeholder': ' Nombres'}),
					'apellido_paterno': forms.TextInput(attrs={'placeholder': 'Apellido Paterno'}),
					'apellido_materno': forms.TextInput(attrs={'placeholder': 'Apellido Materno'}),
					'dni': forms.TextInput(attrs={'placeholder': 'DNI'}),
					'telefono': forms.TextInput(attrs={'placeholder': 'Telefono'}),
					'correo': forms.TextInput(attrs={'placeholder': 'Correo'}),}
