from django import forms
from .models import NavbarItem, quienesSomos, Service

class NavbarItemForm(forms.ModelForm):
    class Meta:
        model = NavbarItem
        fields = ['title', 'url']

class quienesSomosForm(forms.ModelForm):
    class Meta:
        model = quienesSomos
        fields = ['title', 'description']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'image']
