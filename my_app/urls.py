from django.urls import path
from . import views

urlpatterns = [
    # Home landing page
    path('', views.home, name = 'home'),
    
    # Project CRUD paths
    path('projects/', views.index, name = 'index'),
    path('projects/<int:pk>/', views.detail, name = 'detail'),
    path('projects/new/', views.create, name = 'create'),
    path('projects/<int:pk>/edit/', views.update, name = 'update'),
    path('projects/<int:pk>/delete/', views.delete, name = 'delete'),
]