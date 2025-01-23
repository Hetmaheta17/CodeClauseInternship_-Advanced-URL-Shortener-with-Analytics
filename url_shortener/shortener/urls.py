from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_url/', views.create_short_url, name='create_url'),
    path('<str:short_url>/', views.redirect_url, name='redirect_url'),
    path('delete/<str:short_url>/', views.delete_short_url, name='delete_short_url'),
]
