from django.urls import path

from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path('home/', views.home, name="home"),
    path("add_password/", views.add_password, name='add_password'),
    path('add-category/', views.add_password_category, name='add_password_category'),
    path('password_vault/', views.list_passwords, name='password_vault'),
    path('password_vault/edit/<int:password_id>/', views.edit_password, name='edit_password'),
    path('password_vault/delete/<int:password_id>/', views.delete_password, name='delete_password'),
    path('generate_password/', views.generate_password, name='generate_password'),
    path('security_tips/', views.security_tips, name='security_tips')
]
