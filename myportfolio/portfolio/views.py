from django.shortcuts import render
from django.http import Http404

# Bring in Models
from .models import Project

# Create your views here.

def portfolio(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'myportfolio/portfolio.html', context)

def create_img_path(project):
    project["imagePath"] = "/images/" + project["imagePath"]
    project["fullImagePath"]="/images/" + project["fullImagePath"]
