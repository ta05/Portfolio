from django.contrib import admin
from django.urls import path
from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio, name="portfolio"),
    path('<int:project_id>/', views.project, name="project")
]