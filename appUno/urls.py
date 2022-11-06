from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('contactos', views.contactos, name='contactos'),
    path('contactos/crear', views.crear_contacto, name='crear_contacto'),
    path('contactos/editar', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:cedula>', views.eliminar_contacto, name='eliminar_contacto'),
    path('contactos/editar/<int:id>', views.editar_contacto, name='editar_contacto'),
    path('apuntes', views.apuntes, name='apuntes'),
    path('apuntes/crear', views.crear_apunte, name='crear_apunte'),
    path('apuntes/editar', views.editar_apunte, name='editar_apunte'),
    path('eliminar/<int:id>', views.eliminar_apunte, name='eliminar_apunte'),
    path('apuntes/editar/<int:id>', views.editar_apunte, name='editar_apunte'),
]