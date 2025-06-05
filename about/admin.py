from django.contrib import admin
from .models import Biography, Education, WorkExperience

@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date')
    list_filter = ('institution',)
    search_fields = ('institution', 'degree', 'description')

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date')
    list_filter = ('company',)
    search_fields = ('company', 'position', 'description')
