from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project, Profile
from . import views
from .forms import ProjectForm
from django.db.models import Q
from .utils import searchProjects, paginateProjects
from django.contrib import messages



def projects(request):
    projects, search_query = searchProjects(request) 
    custom_range, projects = paginateProjects(request, projects, 4)

    context = {
        'projects': projects,
        'search_query': search_query,
        'custom_range': custom_range,
        }

    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    context = {'project': projectObj} 
    if request.method == 'POST':
        return redirect('project', pk=projectObj.id)

    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, 'Your project has been successfully published')
            return redirect('account')
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form': form, 'project':project}
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    return render(request, 'projects/update-project.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    
    if request.method == "POST":
        project.delete()
        messages.success(request, 'Project was successfully deleted')
        return redirect('account')
    context = {'object': project}
    return render(request, 'projects/delete_project.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile':profile}
    return render(request, 'users/user-profile.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}

    return render(request, 'users/profiles.html', context)
