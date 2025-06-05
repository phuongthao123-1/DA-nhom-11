from django.shortcuts import render, get_object_or_404
from .models import Project

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'title': 'Elon Musk - Dự án',
        'projects': projects
    })

def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    return render(request, 'projects/project_detail.html', {
        'title': f'Elon Musk - {project.title}',
        'project': project
    })
