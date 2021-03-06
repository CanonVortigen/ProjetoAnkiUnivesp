from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexView(TemplateView):
    template_name = 'index.html'
index = IndexView.as_view()


def contact(request):
    success = False        
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)

def help(request):
    return render(request, 'help.html')

def file(request):
    return render(request, 'file.html')

def project(request):
    return render(request, 'project.html')







