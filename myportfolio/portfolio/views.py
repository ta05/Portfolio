from django.shortcuts import render
from django.http import Http404

# Bring in Models
from .models import Project

# Create your views here.

def portfolio(request):
    return render(request, 'myportfolio/portfolio.html')
