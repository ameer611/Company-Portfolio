from PIL import Image
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    return render(
        request=request,
        template_name='../templates/home.html'
    )

def get_services(request):
    services = Services.objects.all()
    context = {
        'services': services,
    }

    return render(
        request=request,
        template_name='../templates/services.html',
        context = context
    )

def get_staffes(request):
    staffes = Staff.objects.all()
    context = {
        'staffes': staffes,
    }

    return render(
        request=request,
        template_name='../templates/staffes.html',
        context = context
    )

def get_contact_us(request):
    contacts = Contact_us.objects.all().order_by('-id')
    if contacts:
        contacts1 = contacts.values()[0]

        return render(
            request=request,
            template_name='../templates/contact.html',
            context={'contacts': contacts1}
        )

    return render(
        request=request,
        template_name='../templates/contact.html',
        context={'contacts': contacts}
    )

def is_image(variable):
    return isinstance(variable, Image.Image)

def get_image(request):
    logo = Logo.objects.all().order_by('-id')
    if is_image(logo.values()[0]):
        logo1 = logo.values()[0]
        return {'logo': logo1}
    return {'logo': logo.first()}


