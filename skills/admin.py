from django.contrib import admin
from .models import SkillCategory, Skill

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'description')
    inlines = [SkillInline]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'level')
    list_filter = ('category', 'level')
    search_fields = ('name', 'description')
    list_editable = ('level',)
