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
from .views import login_view
from .views import home_view
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView

from .views import execute_command_view



urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # home
    path('home/', home_view, name='home'),

    re_path(r'^$', RedirectView.as_view(url='/home/', permanent=False), name='index'), 

    path('execute-command/', execute_command_view, name='execute_command'),


    

]
