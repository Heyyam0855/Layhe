from django.contrib import admin
from django.utils.html import format_html
from .models import ContactMessage, NewsletterSubscription, ContactInfo, SocialMedia


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'email', 'status', 'is_urgent', 'is_responded', 'created_at']
    list_filter = ['status', 'is_urgent', 'is_responded', 'created_at', 'test_type']
    search_fields = ['first_name', 'last_name', 'phone', 'email', 'message']
    list_editable = ['status', 'is_urgent', 'is_responded']
    readonly_fields = ['created_at', 'updated_at', 'full_name']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Şəxsi Məlumatlar', {
            'fields': ('first_name', 'last_name', 'full_name', 'phone', 'email')
        }),
        ('Mesaj Məlumatları', {
            'fields': ('subject', 'test_type', 'preferred_date', 'message')
        }),
        ('Status və İdarəetmə', {
            'fields': ('status', 'is_urgent', 'is_responded', 'admin_notes')
        }),
        ('Tarix Məlumatları', {
            'fields': ('created_at', 'updated_at', 'responded_at'),
            'classes': ('collapse',)
        }),
    )
    
    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Ad Soyad'
    
    actions = ['mark_as_responded', 'mark_as_urgent', 'mark_as_resolved']
    
    def mark_as_responded(self, request, queryset):
        queryset.update(is_responded=True, status='in_progress')
    mark_as_responded.short_description = 'Cavablandırılmış kimi işarələ'
    
    def mark_as_urgent(self, request, queryset):
        queryset.update(is_urgent=True)
    mark_as_urgent.short_description = 'Təcili kimi işarələ'
    
    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved', is_responded=True)
    mark_as_resolved.short_description = 'Həll edilmiş kimi işarələ'


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active', 'subscribed_at', 'unsubscribed_at']
    list_filter = ['is_active', 'subscribed_at']
    search_fields = ['email']
    list_editable = ['is_active']
    readonly_fields = ['subscribed_at', 'unsubscribed_at']
    ordering = ['-subscribed_at']
    date_hierarchy = 'subscribed_at'
    
    actions = ['activate_subscriptions', 'deactivate_subscriptions']
    
    def activate_subscriptions(self, request, queryset):
        queryset.update(is_active=True, unsubscribed_at=None)
    activate_subscriptions.short_description = 'Abunəliyi aktivləşdir'
    
    def deactivate_subscriptions(self, request, queryset):
        from django.utils import timezone
        queryset.update(is_active=False, unsubscribed_at=timezone.now())
    deactivate_subscriptions.short_description = 'Abunəliyi deaktivləşdir'


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'value', 'icon', 'is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'value']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'name']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform', 'username', 'url_link', 'icon', 'is_active', 'order']
    list_filter = ['platform', 'is_active', 'created_at']
    search_fields = ['platform', 'username']
    list_editable = ['is_active', 'order']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['order', 'platform']
    
    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    url_link.short_description = 'URL'
