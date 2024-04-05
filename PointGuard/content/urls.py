from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_password/", views.add_password, name='add_password'),
]
