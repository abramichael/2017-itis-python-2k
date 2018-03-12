"""YandexMusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView, FormView

from music.forms import LoginForm
from music.views import do_login

urlpatterns = [
    url('admin/', admin.site.urls),
    #url('login/', FormView.as_view(template_name="music/login.html", form_class=LoginForm), name="login"),
    url('login/', do_login, name="login"),
    url('music/', include('music.urls')),

]
