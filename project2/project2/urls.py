"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from lnb2.views import create_view, dashboard, delete_view, detail_view, list_view, update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',dashboard),
    path('create/',create_view),
    path('list/',list_view),
    path('<id>/', detail_view ),
    path('<id>/update/', update_view ),
    path('<id>/delete/', delete_view),
]