from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

# Register your models here.
from .models import Project

class ProjectAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Projects"
admin.site.index_title = "Welcome to the Projects Admin Area"

admin.site.register(Project, ProjectAdmin)
