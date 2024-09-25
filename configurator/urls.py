from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('assemblerPC/', views.AssemblerPCView.as_view(), name='assembler_PC'),
    path('computers/', views.PCList.as_view()),
    path('api/price', views.get_price)
]