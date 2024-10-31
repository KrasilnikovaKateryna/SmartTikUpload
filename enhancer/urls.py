from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('profile/', views.profile),
    path('browse/', views.browse),
    path('streams/', views.streams),
]