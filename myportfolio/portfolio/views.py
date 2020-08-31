from django.shortcuts import render
from django.http import Http404

# Bring in Models
from .models import Project

# Create your views here.

# Gets all projects in portfolio and displays them
def portfolio(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'portfolio/portfolio.html', context)

# Gets a specific project and displays it
def project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'portfolio/project.html', {'project': project})
