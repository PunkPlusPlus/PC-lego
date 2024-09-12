from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('assemblerPC', views.AssemblerPCView.as_view(), name='assembler_PC')
]