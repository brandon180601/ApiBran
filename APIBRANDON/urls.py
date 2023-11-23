"""APIBRANDON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from api.views import *
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.iniciar_sesion, name='iniciar_sesion'),
    path('index.html', IndexView.as_view(), name='index'),
    path('icons.html', icons.as_view(), name='icons'),
    path('colors.html', colors.as_view(), name='colors'),
    path('forms.html', forms.as_view(), name='forms'),
    path('calendars.html', calendars.as_view(), name='calendars'),
    path('alerts.html', alerts.as_view(), name='alerts'),
    path('flex.html', flex.as_view(), name='flex'),
    path('getting-started.html', gettingStarted.as_view(), name='gettin-started'),
    path('list.html', list.as_view(), name='list'),
    path('navs.html', navs.as_view(), name='navs'),
    path('panels.html', panels.as_view(), name='panels'),
    path('timeline.html', timeline.as_view(), name='timeline'),
    path('typography.html', typography.as_view(), name='typography'),
    path('registro/', views.registrar_usuario, name='registro'),
    path('graficas/', views.dashboard, name='dashboard'),
    path('maps/', footers.as_view(), name='maps'),
    path('Perfil1/', persona1.as_view(), name='persona1'),
    path('Perfil2/', persona2.as_view(), name='persona2'),
    path('Perfil3/', persona3.as_view(), name='persona3'),
    path('Perfil4/', persona4.as_view(), name='persona4')
]
