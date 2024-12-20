from django.urls import path
from . import views

urlpatterns = [
    path('say_hello/', views.say_hello, name='say_hello'),
    path('getapi/', views.getdata, name='getdata'),
    path('postapi/', views.postdata, name='postdata'),
    path('putapi/<int:pk>/', views.putdata, name='putdata'),
    path('patchapi/<int:pk>/', views.patchdata, name='patchdata'),
    path('deleteapi/<int:pk>/', views.deletedata, name='deletedata'),
    path('employeeapi/', views.EmployeeApiView.as_view(), name='employeeapi'),
]