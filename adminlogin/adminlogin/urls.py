"""
URL configuration for adminlogin project.

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
from django.urls import path
from login import views  
from uploadvideo import views as uploadvideo_views  
from devices import views as devies_data

urlpatterns = [
    path('admin/login/', views.adminLoginApi, name='admin-login-api'),  
    path('media/', uploadvideo_views.upload, name='media_list'),  
    path('devices/',devies_data.DevicesApi,name='devies_data')
    
]
