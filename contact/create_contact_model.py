from django import forms
from django.core.exceptions import ValidationError

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta: 
        model = Contact
        fields = ('first_name', 'last_name', 'phone')
    
    def clean(self):
        
        self.add_error(
            'first_name', ValidationError('Error message', code='invalid')
        )

        return super().clean()