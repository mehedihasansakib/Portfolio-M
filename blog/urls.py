from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]