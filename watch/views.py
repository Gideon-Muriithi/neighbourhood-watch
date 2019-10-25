from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def index(request):
    title = 'Home'
    return render(request, 'index.html', {'title':title})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})
