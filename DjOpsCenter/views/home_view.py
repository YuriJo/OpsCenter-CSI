from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import subprocess
from DjOpsCenter.forms import LoginForm
from DjOpsCenter.models import Clients, Commands

##############################################################################################################



@login_required
def home_view(request):
    # Создаем контекст, который будет отправлен в шаблон
    context = {}
    context['test_clients_output'] = ['Test Client 1', 'Test Client 2', 'Test Client 3']

    # Если это запрос на получение списка клиентов
    if request.method == 'POST' and 'list_clients' in request.POST:
        clients = Clients.objects.all().order_by('name')  # Получаем всех клиентов, отсортированных по имени
        context['clients'] = clients  # Добавляем клиентов в контекст

    return render(request, 'home.html', context)