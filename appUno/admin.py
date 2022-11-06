from django.contrib import admin
from .models import Contacto
from .models import Apuntes

class AdminContacto(admin.ModelAdmin):
	list_display=["__str__","nombre","apellido","celular","cedula","email"]
	class Meta(object):
		model = Contacto


class AdminApuntes(admin.ModelAdmin):
	list_display=["__str__","nombre","contenido"]
	class Meta(object):
		model = Apuntes

admin.site.register(Contacto,AdminContacto)
admin.site.register(Apuntes,AdminApuntes)
