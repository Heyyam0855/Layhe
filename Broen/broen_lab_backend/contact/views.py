from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ContactMessage, NewsletterSubscription, ContactInfo, SocialMedia
from .serializers import (ContactMessageSerializer, NewsletterSubscriptionSerializer, 
                         ContactInfoSerializer, SocialMediaSerializer)


class ContactMessageCreateView(generics.CreateAPIView):
    """Əlaqə mesajı yaratma"""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer


class NewsletterSubscriptionCreateView(generics.CreateAPIView):
    """Newsletter abunəliyi"""
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer


class ContactInfoListView(generics.ListAPIView):
    """Aktiv əlaqə məlumatları"""
    queryset = ContactInfo.objects.filter(is_active=True)
    serializer_class = ContactInfoSerializer


class SocialMediaListView(generics.ListAPIView):
    """Aktiv sosial media hesabları"""
    queryset = SocialMedia.objects.filter(is_active=True)
    serializer_class = SocialMediaSerializer


@api_view(['POST'])
def contact_form_submit(request):
    """Əlaqə formu göndərmə (frontend üçün)"""
    serializer = ContactMessageSerializer(data=request.data)
    
    if serializer.is_valid():
        contact_message = serializer.save()
        return Response({
            'success': True,
            'message': 'Mesajınız uğurla göndərildi. Tezliklə sizinlə əlaqə saxlayacağıq.',
            'data': ContactMessageSerializer(contact_message).data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'message': 'Məlumatları yoxlayın və yenidən cəhd edin.',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def newsletter_subscribe(request):
    """Newsletter abunəliyi"""
    serializer = NewsletterSubscriptionSerializer(data=request.data)
    
    if serializer.is_valid():
        subscription = serializer.save()
        return Response({
            'success': True,
            'message': 'Newsletter abunəliyiniz uğurla tamamlandı.',
            'data': NewsletterSubscriptionSerializer(subscription).data
        }, status=status.HTTP_201_CREATED)
    
    return Response({
        'success': False,
        'message': 'Email ünvanını yoxlayın.',
        'errors': serializer.errors
    }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def contact_page_data(request):
    """Əlaqə səhifəsi məlumatları"""
    try:
        contact_info = ContactInfo.objects.filter(is_active=True)
        social_media = SocialMedia.objects.filter(is_active=True)
        
        return Response({
            'contact_info': ContactInfoSerializer(contact_info, many=True).data,
            'social_media': SocialMediaSerializer(social_media, many=True).data,
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)
