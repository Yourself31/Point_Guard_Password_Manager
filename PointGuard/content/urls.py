from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path('home/', views.home, name="home"),
    path("add_password/", views.add_password, name='add_password'),
    path('add-category/', views.add_password_category, name='add_password_category'),
    path('access_passwords/', views.access_passwords, name='access_passwords'),
    path('generate_password/', views.generate_password, name='generate_password'),
    path('security_tips/', views.security_tips, name='security_tips')
]
