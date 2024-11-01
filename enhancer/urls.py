from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
    path('profile/', views.profile),
    path('privacy/', views.browse),
    path('terms/', views.streams),
    path('verify/', views.verify),
]