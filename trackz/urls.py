from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_profiles, name='get_profiles'),
    path('get_profile/<int:pk>/', views.get_profile, name='get_profile'),
]
