from django.contrib import admin
from .models import Project, Experiment

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'created_at')
    list_filter = ('status', 'user')
    search_fields = ('name', 'description')

@admin.register(Experiment)
class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'user', 'status', 'start_date')
    list_filter = ('status', 'user', 'project')
    search_fields = ('title', 'objective', 'lead_researcher')
