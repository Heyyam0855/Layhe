from rest_framework import serializers
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, NewsletterSubscription, ContactInfo, SocialMedia


class ContactMessageSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = ContactMessage
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 
                 'subject', 'test_type', 'preferred_date', 'message', 
                 'full_name', 'created_at']
        read_only_fields = ['id', 'full_name', 'created_at']
    
    def create(self, validated_data):
        # Mesaj yaradılarkən admin-ə email göndər
        contact_message = super().create(validated_data)
        
        try:
            subject = f"Yeni əlaqə mesajı - {contact_message.full_name}"
            message = f"""
Yeni əlaqə mesajı alındı:

Ad Soyad: {contact_message.full_name}
Telefon: {contact_message.phone}
Email: {contact_message.email}
Mövzu: {contact_message.subject or 'Mövzu qeyd edilməyib'}
Test növü: {contact_message.test_type or 'Qeyd edilməyib'}
Üstünlük verilən tarix: {contact_message.preferred_date or 'Qeyd edilməyib'}

Mesaj:
{contact_message.message}

Tarix: {contact_message.created_at.strftime('%d.%m.%Y %H:%M')}
            """
            
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['admin@broen.az'],  # Admin email-i
                fail_silently=True,
            )
        except Exception:
            # Email göndərmə xətası olsa belə, mesaj saxlanılsın
            pass
            
        return contact_message


class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['id', 'email', 'subscribed_at']
        read_only_fields = ['id', 'subscribed_at']
    
    def create(self, validated_data):
        # Əgər email artıq mövcuddursa, yenidən aktivləşdir
        email = validated_data['email']
        subscription, created = NewsletterSubscription.objects.get_or_create(
            email=email,
            defaults=validated_data
        )
        
        if not created and not subscription.is_active:
            subscription.is_active = True
            subscription.unsubscribed_at = None
            subscription.save()
            
        return subscription


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    platform_display = serializers.CharField(source='get_platform_display', read_only=True)
    
    class Meta:
        model = SocialMedia
        fields = '__all__'