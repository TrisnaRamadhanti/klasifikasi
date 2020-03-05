"""ProjectTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from crudapp import views
from crudapp1 import views as viewscrudapp1

urlpatterns = [
    path('admin/', admin.site.urls),

    path('data/', viewscrudapp1.IndexView.as_view(), name='index'),
    path('data/<int:pk>/', viewscrudapp1.DataDetailView.as_view(), name='detail'),
    path('data/edit/<int:pk>/', viewscrudapp1.edit, name='edit'),
    path('data/create/', viewscrudapp1.create, name='create'),
    path('data/delete/<int:pk>/', viewscrudapp1.delete, name='delete'),
]