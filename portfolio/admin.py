from django.contrib import admin
from .models import PortfolioCategory, PortfolioItem, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'completion_date', 'is_featured', 'created_at')
    list_filter = ('category', 'completion_date', 'is_featured')
    search_fields = ('title', 'description', 'client')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    list_editable = ('is_featured',)
    inlines = [PortfolioImageInline]

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ('portfolio_item', 'caption', 'order')
    list_filter = ('portfolio_item',)
    list_editable = ('order',)
