from django.contrib import admin
from .models import TestCategory, Test, TestPackage


@admin.register(TestCategory)
class TestCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'is_active', 'order', 'created_at']
    list_filter = ['category_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'name']


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'category', 'price', 'discount_price', 'is_popular', 'is_active']
    list_filter = ['category', 'is_popular', 'is_active', 'created_at']
    search_fields = ['name', 'code', 'description']
    list_editable = ['price', 'discount_price', 'is_popular', 'is_active']
    readonly_fields = ['created_at', 'updated_at', 'effective_price', 'has_discount']
    ordering = ['category', 'order', 'name']
    
    fieldsets = (
        ('Əsas Məlumatlar', {
            'fields': ('name', 'code', 'category', 'description')
        }),
        ('Test Təfərrüatları', {
            'fields': ('sample_type', 'result_time', 'preparation_info', 'normal_range')
        }),
        ('Qiymət Məlumatları', {
            'fields': ('price', 'discount_price', 'effective_price', 'has_discount')
        }),
        ('Parametrlər', {
            'fields': ('is_popular', 'is_active', 'order')
        }),
        ('Tarix Məlumatları', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TestPackage)
class TestPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'package_price', 'discount_percentage', 'is_featured', 'is_active']
    list_filter = ['is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['package_price', 'is_featured', 'is_active']
    filter_horizontal = ['tests']
    readonly_fields = ['created_at', 'updated_at', 'individual_total_price', 'savings_amount']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Paket Məlumatları', {
            'fields': ('name', 'description')
        }),
        ('Testlər', {
            'fields': ('tests',)
        }),
        ('Qiymət Məlumatları', {
            'fields': ('package_price', 'discount_percentage', 'individual_total_price', 'savings_amount')
        }),
        ('Parametrlər', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
        ('Tarix Məlumatları', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
