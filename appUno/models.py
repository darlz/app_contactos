from django.db import models

# Create your models here.
class Contacto(models.Model):
	nombre=models.CharField(max_length=30)
	apellido=models.CharField(max_length=30)
	celular=models.CharField(max_length=10)
	cedula=models.CharField(max_length=30)
	email=models.CharField(max_length=30)
	def __str__(self):
		return self.cedula

class Apuntes(models.Model):
	cedula=models.ForeignKey(Contacto, on_delete=models.CASCADE)
	nombre=models.CharField(max_length=30)
	contenido=models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

 
