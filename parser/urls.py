from django.urls import path
from . import views

urlpatterns = [
    path('components', views.components, name='components'),
    path('matching_table', views.matching_table, name='matching_table'),
    path('source', views.source, name='source'),
]