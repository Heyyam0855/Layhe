from django.contrib import admin
from .models import Company, Service, TeamMember, FAQ


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'established_year', 'created_at']
    list_filter = ['created_at', 'established_year']
    search_fields = ['name', 'phone', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Əsas Məlumatlar', {
            'fields': ('name', 'description', 'logo')
        }),
        ('Missiya və Vizyon', {
            'fields': ('mission', 'vision'),
            'classes': ('collapse',)
        }),
        ('Əlaqə Məlumatları', {
            'fields': ('address', 'phone', 'email', 'working_hours')
        }),
        ('Digər Məlumatlar', {
            'fields': ('established_year',)
        }),
        ('Tarix Məlumatları', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'title']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position', 'specialization', 'experience_years', 'is_active', 'order']
    list_filter = ['position', 'is_active', 'created_at']
    search_fields = ['full_name', 'specialization', 'description']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'full_name']
    
    fieldsets = (
        ('Şəxsi Məlumatlar', {
            'fields': ('full_name', 'position', 'photo')
        }),
        ('Peşəkar Məlumatlar', {
            'fields': ('specialization', 'experience_years', 'description')
        }),
        ('Parametrlər', {
            'fields': ('is_active', 'order')
        }),
        ('Tarix Məlumatları', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['question', 'answer']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'question']
