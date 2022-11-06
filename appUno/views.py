from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacto, Apuntes
from .forms import ContactoForm, ApunteForm

def inicio(request):
	return render(request, 'paginas/inicio.html')

def contactos(request):
	contactos=Contacto.objects.all()
	#print(contactos)
	return render(request, 'contactos/index.html', {'contactos': contactos})

def crear_contacto(request):
	formulario = ContactoForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
		return redirect('contactos')
	return render(request, 'contactos/crear.html', {'formulario': formulario})

def editar_contacto(request, id):
	contacto=Contacto.objects.get(id=id)
	formulario=ContactoForm(request.POST or None, instance=contacto)
	if formulario.is_valid() and request.POST:
		formulario.save()
		return redirect('contactos')
	return render(request, 'contactos/editar.html', {'formulario':formulario})

def eliminar_contacto(request, cedula):
	contacto =Contacto.objects.get(cedula=cedula)
	contacto.delete()
	return redirect('contactos')

#views Apuntes
def apuntes(request):
	apuntes=Apuntes.objects.all()
	#print(apuntes)
	return render(request, 'apuntes/index.html', {'apuntes': apuntes})

def crear_apunte(request):
	formulario = ApunteForm(request.POST or None)
	if formulario.is_valid():
		formulario.save()
		return redirect('apuntes')
	return render(request, 'apuntes/crear.html', {'formulario': formulario})

def editar_apunte(request, id):
	print(type(id))
	apunte=Apuntes.objects.get(id=id)
	formulario=ApunteForm(request.POST or None, instance=apunte)
	if formulario.is_valid() and request.POST:
		formulario.save()
		return redirect('apuntes')
	return render(request, 'apuntes/editar.html', {'formulario':formulario})

def eliminar_apunte(request, id):
	apunte =Apuntes.objects.get(id=id)
	apuntes.delete()
	return redirect('apuntes')