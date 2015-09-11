from django.shortcuts import render
from .models import RegistroForm
from .models import Registro
from .models import CitaForm
from .models import Cita
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template import loader, Context
from django.template.loader import get_template
from django import forms

def registro(request):
	if request.method == "POST":
		form = RegistroForm(request.POST)
		tipo = str(request.POST['tipo_persona'])
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			if (tipo =='V'):
				registros=Registro.objects.filter(tipo_persona='V').last()
				return redirect('registro.views.cita', pk=registros.pk)
			else:	
				return redirect('registro.views.index')
		else:
			form = RegistroForm(request.POST)
			return render(request,'registro/registro.html', {'form': form})

	else: 
		form = RegistroForm()
		return render(request,'registro/registro.html', {'form': form})



def index(request):
	if request.method == "POST":
		dni=request.POST['buscar']
		if Registro.objects.filter(dni=dni).exists():
			id_revision = Registro.objects.filter(dni=dni).last()
			print id_revision.pk
			return redirect('registro.views.cita', pk=id_revision.pk)
		else:
			return redirect('registro.views.registro')


	else:
		return render(request,'registro/index.html')


def cita(request, pk):
	if request.method == "POST":
		registros=Registro.objects.filter(id=pk).last()
		buscar= str(request.POST['buscar'])
		cita=Cita(registros=registros,buscar=buscar)
		cita = cita.save()
		return redirect('registro.views.index')

	else:
		registro = get_object_or_404(Registro, pk=pk)
		if Registro.objects.all().count()>0 :
			nombres = registro.nombres
			apellido_paterno = registro.apellido_paterno
			apellido_materno = registro.apellido_materno
			form = CitaForm( initial= {'nombres':nombres,'apellido_paterno':apellido_paterno,'apellido_materno':apellido_materno})

		return render(request,'registro/cita.html', {'form': form})
