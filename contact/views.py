from django.shortcuts import render
# Create your views here.


def index(request):
    print()
    return render(request, 'contact/index.html')
