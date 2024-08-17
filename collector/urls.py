from django.urls import path
from . import views

urlpatterns = [
    path('components', views.components, name='components'),
    path('matching_table', views.matching_table, name='matching_table'),
    path('assembly_pc', views.assembly_pc, name='assembly_pc'),
]