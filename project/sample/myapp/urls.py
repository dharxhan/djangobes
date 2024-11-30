from django.urls import path

from . import views

urlpatterns = [
    path("app/", views.index, name="index"),
    path("ctable/", views.ctable, name="ctable"),
]