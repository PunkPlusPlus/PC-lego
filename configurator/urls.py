from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cpus', views.ApiCpuViewSet)

urlpatterns = [
    path('home_page/', views.HomePageView.as_view(), name='home_page'),
    path('assemblerPC/', views.AssemblerPCView.as_view(), name='assembler_PC'),
    path('computers/', views.PCList.as_view(), name='computers'),
    path('api/price', views.get_price),
    path('api/', include(router.urls)),
]