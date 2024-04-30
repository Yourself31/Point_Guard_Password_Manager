from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add_password/", views.add_password, name='add_password'),
    path('add-category/', views.add_password_category, name='add_password_category')
]
