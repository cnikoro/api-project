"""project URL Configuration

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

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Employee endpoints
    path('employee_list/', views.employee_list, name="employee_list"),
    path('employee_detail/<int:pk>', views.employee_detail, name="employee_detail"),
    path('employee_create/', views.employee_create, name="employee_create"),
    path('employee_update/<int:pk>', views.employee_update, name="employee_update"),
    path('employee_delete/<int:pk>', views.employee_delete, name="employee_delete"),
    
    # Department endpoints
    path('department_list/', views.department_list, name="department_list"),
    path('department_detail/<int:pk>', views.department_detail, name="department_detail"),
    path('department_create/', views.department_create, name="department_create"),
    path('department_update/<int:pk>', views.department_update, name="department_update"),
    path('department_delete/<int:pk>', views.department_delete, name="department_delete"),
]
