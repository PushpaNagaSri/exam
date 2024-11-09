from django.urls import path
from . import views  # Import your views here

urlpatterns = [
    # Example of a valid URL pattern
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),# Ensure this is a valid path and view
    
]
