from django.shortcuts import render, redirect, get_object_or_404
from .models import NavbarItem, quienesSomos, Service
from .forms import NavbarItemForm, QuienesSomosForm, ServiceForm

# Vistas para las páginas principales
def home(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'main/home.html', {'navbar_items': navbar_items, 'services': services})
def quienesSomos(request):
    navbar_items = NavbarItem.objects.all()
    quienesSomos_info = quienesSomos.objects.all()
    return render(request, 'main/quienesSomos.html', {'navbar_items': navbar_items, 'quienesSomos_info': quienesSomos_info})

def services(request):
    navbar_items = NavbarItem.objects.all()
    services = Service.objects.all()
    return render(request, 'main/services.html', {'navbar_items': navbar_items, 'services': services})




