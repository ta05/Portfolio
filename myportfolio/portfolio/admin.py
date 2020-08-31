from django.contrib import admin

# Register your models here.
from .models import Project

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Projects"
admin.site.index_title = "Welcome to the Projects Admin Area"

admin.site.register(Project)
