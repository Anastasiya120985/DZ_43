"""
URL configuration for Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from Django import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.current_date_time, name='current_date_time'),
    path('multiply/', views.multiply, name='multiply'),
    path('multiply/<path:wrong>', views.multiply_, name='multiply_'),
    path('programmday/', views.programmers_day, name='programmers_day'),
    path('programmday/<path:wrong>', views.programmers_day_, name='programmers_day_')
]
