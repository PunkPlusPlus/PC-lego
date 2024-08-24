from django.urls import path
import configurator.views as views

urlpatterns = [
    path('', views.create_component, name='component'),
]