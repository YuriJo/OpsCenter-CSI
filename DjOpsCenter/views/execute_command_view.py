from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import subprocess
from DjOpsCenter.forms import LoginForm
from DjOpsCenter.models import Clients, Commands

####################################################################################################

# Словарь команд
COMMANDS = {
    'cmd1': ['pwd'],
    'cmd2': ['ls', '-lah'],
    'cmd3': ['python', 'manage.py', 'scan_hosts', 'list'],
    'cmd4': ['python', 'manage.py', 'scan_hosts', 'product'],
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
