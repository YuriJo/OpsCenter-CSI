from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import subprocess



def login_view(request):
    form = LoginForm(request.POST or None)
    message = ''
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Измените на нужный URL
        else:
            message = 'Неверный логин или пароль'

    return render(request, 'login.html', {'form': form, 'message': message})

@login_required
def home_view(request):
    return render(request, 'home.html')





# Словарь команд
COMMANDS = {
    'cmd1': ['pwd'],
    'cmd2': ['ls', '-lah'],
    # Добавьте больше команд здесь
}

@login_required
def execute_command_view(request):
    if request.method == 'POST':
        command_key = request.POST.get('command')
        command = COMMANDS.get(command_key)
        
        if command:
            # ВАЖНО: Здесь нет необходимости в shell=True, так как мы не принимаем произвольный ввод
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            return JsonResponse({'output': output})
        else:
            return JsonResponse({'error': 'Invalid command'}, status=400)
    else:
        # GET запрос - просто отобразите страницу с формой
        return render(request, 'home.html')


