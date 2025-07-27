from django.urls import path
from . import views

app_name = 'protfolio'  # Add this line
urlpatterns = [
    path('', views.home, name='home'),
]