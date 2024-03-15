from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contact.create_contact_model import RegisterForm, RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm 


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('contact:index')
        
    return render(request, 'contact/register.html',
                  {
                      'form': form
                  })

def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Logged successufully!")
            return redirect('contact:index')
        else:
            messages.error(request, "Invalid input")
    return render(request, 'contact/login.html', {
        'form': form
    })

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
            request,
            'contact/register.html',
            {'form': form}
        )
    form = RegisterUpdateForm(data=request.POST, instance=request.user,)

    if form.is_valid():
        form.save()
    return render(
            request,
            'contact/register.html',
            {'form': form}
        )