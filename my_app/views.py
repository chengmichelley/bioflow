from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status']

def home(request):
    return render(request, 'bioflow/home.html')

def index(request):
    projects = Project.objects.all()
    return render(request, 'bioflow/project_index.html', { 'projects': projects })

def detail(request, pk):
    project = get_object_or_404(Project, pk = pk)
    return render(request, 'bioflow/project_detail.html', { 'project': project})

def create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'bioflow/project_form.html', { 'form':form })
    
def update(request, pk):
    project = get_object_or_404(Project, pk = pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return redirect('detail', pk = project.pk)
    else:
        form = ProjectForm(instance = project)
    return render(request, 'bioflow/project_form.html', { 'form': form, 'project': project })

def delete(request, pk):
    project = get_object_or_404(Project, pk = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('index')
    return render(request, 'bioflow/project_confirm_delete.html', { 'project': project})