from typing import Any, Mapping
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from contact.models import Contact

class ContactForm(forms.ModelForm):
    # Outra opção de mudar widgets
    # def __init__(self, *args, **kwargs):
    #     super().__init__(**args, **kwargs)

    #     self.fields['first_name'].widgets.attrs.update({'placeholder' : 'Write first name'})
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        )
    )
    class Meta: 
        model = Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture')
        
    
    def clean(self):
        #  Retorna clean do super
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError("First name cannot be equal to last name.", code='invalid')
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()
    
    # def clean_first_name(self):
    #     first_name = self.cleaned_data.get('first_name')

    #     if first_name == 'ABC':
    #         self.add_error(
    #             'first_name',
    #             ValidationError(
    #                 'Veio do add_error',
    #                 code='invalid'
    #             )
    #         )