from django.contrib import admin
from django.contrib import admin
from .models import Project, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_completed')
    list_filter = ('categories', 'date_completed')
    search_fields = ('title', 'description')
    filter_horizontal = ('categories',)

# Register your models here.
