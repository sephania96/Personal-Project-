from django.contrib import admin
from projects.models import project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(project, ProjectAdmin)