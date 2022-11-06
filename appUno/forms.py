from django import forms
from .models import Contacto, Apuntes

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

class ApunteForm(forms.ModelForm):
    class Meta:
        model= Apuntes
        fields='__all__'
        