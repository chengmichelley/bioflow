from django.urls import path
from . import views

urlpatterns = [
    # Home landing page
    path('', views.home, name = 'home'),
    
    # Project CRUD paths
    path('projects/', views.project_index, name = 'project_index'),
    path('projects/<int:pk>/', views.project_detail, name = 'project_detail'),
    path('projects/new/', views.project_create, name = 'project_create'),
    path('projects/<int:pk>/edit/', views.project_update, name = 'project_update'),
    path('projects/<int:pk>/delete/', views.project_delete, name = 'project_delete'),
    
    # Experiment CRUD paths
    path('experiments/', views.experiment_index, name = 'experiment_index'),
    path('experiments/<int:pk>/', views.experiment_detail, name = 'experiment_detail'),
    path('experiments/new/', views.experiment_create, name = 'experiment_create'),
    path('experiments/<int:pk>/edit/', views.experiment_update, name = 'experiment_update'),
    path('experiments/<int:pk>/delete/', views.experiment_delete, name = 'experiment_delete'),
]
