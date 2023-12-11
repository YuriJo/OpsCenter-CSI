from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import subprocess
from DjOpsCenter.forms import LoginForm
from DjOpsCenter.models import Clients, Commands

##############################################################################################################



def login_view(request):
    form = LoginForm(request.POST or None)
    message = ''
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password') 
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            message = 'Неверный логин или пароль'

    return render(request, 'login.html', {'form': form, 'message': message})