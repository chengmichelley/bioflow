from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Experiment
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status']

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description']

def home(request):
    return render(request, 'bioflow/home.html')

# Projects

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'bioflow/project_index.html', { 'projects': projects })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk = pk)
    return render(request, 'bioflow/project_detail.html', { 'project': project})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_index')
    else:
        form = ProjectForm()
    return render(request, 'bioflow/project_form.html', { 'form':form })
    
def project_update(request, pk):
    project = get_object_or_404(Project, pk = pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance = project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk = project.pk)
    else:
        form = ProjectForm(instance = project)
    return render(request, 'bioflow/project_form.html', { 'form': form, 'project': project })

def project_delete(request, pk):
    project = get_object_or_404(Project, pk = pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_index')
    return render(request, 'bioflow/project_confirm_delete.html', { 'project': project})

# Experiments

def experiment_index(request):
    experiment = Experiment.objects.all()
    return render(request, 'bioflow/experiment_index.html', { 'experiments': experiment })

def experiment_detail(request, pk):
    experiment = get_object_or_404(Experiment, pk = pk)
    return render(request, 'bioflow/experiment_detail.html', { 'experiment': experiment})

def experiment_create(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experiment_index')
    else:
        form = ExperimentForm()
    return render(request, 'bioflow/experiment_form.html', { 'form': form })
    
def experiment_update(request, pk):
    experiment = get_object_or_404(Experiment, pk = pk)
    if request.method == 'POST':
        form = ExperimentForm(request.POST, instance = experiment)
        if form.is_valid():
            form.save()
            return redirect('experiment_detail', pk = experiment.pk)
    else:
        form = ExperimentForm(instance = experiment)
    return render(request, 'bioflow/experiment_form.html', { 'form': form, 'experiment': experiment })

def experiment_delete(request, pk):
    experiment = get_object_or_404(Experiment, pk = pk)
    if request.method == 'POST':
        experiment.delete()
        return redirect('experiment_index')
    return render(request, 'bioflow/experiment_confirm_delete.html', { 'experiment': experiment})
