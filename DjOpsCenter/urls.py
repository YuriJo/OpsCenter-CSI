"""
URL configuration for DjOpsCenter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

from DjOpsCenter.views.execute_command_view import execute_command_view
from DjOpsCenter.views.login_view import login_view
from DjOpsCenter.views.home_view import home_view
from DjOpsCenter.views.list_clients_view import list_clients_view



urlpatterns = [
    path("admin/", admin.site.urls),                                                   # Админка
    path('login/', login_view, name='login'),                                          # Страница входа
    path('logout/', LogoutView.as_view(), name='logout'),                              # Страница выхода
    path('home/', home_view, name='home'),                                             # Главная страница
    re_path(r'^$', RedirectView.as_view(url='/home/', permanent=False), name='index'), # Перенаправление на главную страницу
    path('execute-command/', execute_command_view, name='execute_command'),            # Страница выполнения команды
    path('list-clients/', list_clients_view, name='list_clients'),                     # Страница списка клиентов


    

]
