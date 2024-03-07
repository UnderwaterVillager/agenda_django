from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError

from contact.models import Contact
# Create your views here.

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ('first_name', 'last_name', 'phone')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            None, ValidationError('Error message', code='invalid')
        )

        return super().clean()

def create(request):
    if request.method == "POST":
        context = {
            'form': ContactForm(request.POST),
        }
        return render(request, 'contact/create.html', context)
    
    context = {
            'form': ContactForm(request.POST),
        }
    return render(request, 'contact/create.html', context)