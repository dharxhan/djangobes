# moduleformapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('employee/create/', views.employee_create, name='employee_create'),
    path('success/', views.success_view, name='success'),
]
