from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_profiles, name='get_profiles'),
    path('<int:pk>/', views.get_profile, name='get_profile'),
]
