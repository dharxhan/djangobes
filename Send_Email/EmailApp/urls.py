from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribeuser, name='Subscriber'),
]