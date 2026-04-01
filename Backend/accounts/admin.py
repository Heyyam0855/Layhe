from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['ad', 'soyad', 'get_email', 'telefon', 'qeyd_tarixi']
    list_filter = ['qeyd_tarixi', 'yenileme_tarixi']
    search_fields = ['ad', 'soyad', 'user__email']
    date_hierarchy = 'qeyd_tarixi'
    ordering = ['-qeyd_tarixi']

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'
