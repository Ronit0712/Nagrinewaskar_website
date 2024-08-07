"""
URL configuration for FoundationProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from userApp import views

urlpatterns = [
    path('admin/', include('adminApp.admin_urls')),
    path('',views.home),
    path('save_form/', views.save_form),
    path('mission/',views.mission),
    path('vision/',views.vision),
    path('history/',views.history),
    path('gallery/',views.gallery),
    path('activities/',views.activities),
    path('achievements/',views.achievements),
    path('contact/',views.contact),
    path('save_contact/',views.save_contact),
   

]
  