from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Experiment
from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status']

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['project', 'title', 'objective', 'lead_researcher', 'status', 'start_date', 'end_date']

def home(request):
    if request.user.is_authenticated:
        return render(request, 'bioflow/home.html')
    
    form = AuthenticationForm()
    return render(request, 'bioflow/home.html', {'form': form})

@login_required
def project_index(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'bioflow/project_index.html', { 'projects': projects })

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    return render(request, 'bioflow/project_detail.html', { 'project': project})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_index')
    else:
        form = ProjectForm()
    return render(request, 'bioflow/project_form.html', { 'form':form })
    
@login_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'bioflow/project_form.html', { 'form': form, 'project': project })

@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('project_index')
    return render(request, 'bioflow/project_confirm_delete.html', { 'project': project})

@login_required
def experiment_index(request):
    experiments = Experiment.objects.filter(user=request.user)
    return render(request, 'bioflow/experiment_index.html', { 'experiments': experiments })

@login_required
def experiment_detail(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk, user=request.user)
    return render(request, 'bioflow/experiment_detail.html', { 'experiment': experiment})

@login_required
def experiment_create(request):
    if request.method == 'POST':
        form = ExperimentForm(request.POST)
        if form.is_valid():
            experiment = form.save(commit=False)
            experiment.user = request.user
            experiment.save()
            return redirect('experiment_index')
    else:
        form = ExperimentForm()
    return render(request, 'bioflow/experiment_form.html', { 'form': form })
    
@login_required
def experiment_update(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExperimentForm(request.POST, instance=experiment)
        if form.is_valid():
            form.save()
            return redirect('experiment_detail', pk=experiment.pk)
    else:
        form = ExperimentForm(instance=experiment)
    return render(request, 'bioflow/experiment_form.html', { 'form': form, 'experiment': experiment })

@login_required
def experiment_delete(request, pk):
    experiment = get_object_or_404(Experiment, pk=pk, user=request.user)
    if request.method == 'POST':
        experiment.delete()
        return redirect('experiment_index')
    return render(request, 'bioflow/experiment_confirm_delete.html', { 'experiment': experiment})
