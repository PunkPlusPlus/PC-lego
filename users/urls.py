from django.urls import path
from . import views

urlpatterns = [
    path('assembly_pc', views.assembly_pc, name='assembly_pc'),
    path('users', views.users, name='users'),
    path('regform', views.reg_form),
]