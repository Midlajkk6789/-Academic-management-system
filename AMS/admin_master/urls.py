"""
URL configuration for AMS project.

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
from . import views
from django.urls import path

urlpatterns = [
    path('adminClass/', views.adminClass,name='adminClass'),
    path('adminDepartment/', views.adminDepartment,name='adminDepartment'),
    path('editDepartment/', views.editDepartment,name='editDepartment'),
    path('updateDepartment/', views.updateDepartment,name='updateDepartment'),
    path('adminDesignation/', views.adminDesignation,name='adminDesignation'),
    path('adminDivision/', views.adminDivision,name='adminDivision'),
    path('adminEmployeeCatagory/', views.adminEmployeeCatagory,name='adminEmployeeCatagory'),
    path('adminQualification/', views.adminQualification,name='adminQualification'),
    path('deleteDipartment/',views.deleteDipartment,name='deleteDipartment'),
    path('deleteClass/',views.deleteClass,name='deleteClass'),
    path('editClass/',views.editClass,name='editClass'),
    path('updateClass/',views.updateClass,name='updateClass'),
    path('adminSubject/',views.adminSubject,name='adminSubject'),
    path('editSubject/',views.editSubject,name='editSubject'),
]
