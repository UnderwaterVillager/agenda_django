from django.shortcuts import render

from contact.create_contact_model import ContactForm
# Create your views here.



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