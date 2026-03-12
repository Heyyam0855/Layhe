from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from .models import Company, Service, TeamMember, FAQ
from .serializers import CompanySerializer, ServiceSerializer, TeamMemberSerializer, FAQSerializer


class CompanyListView(generics.ListAPIView):
    """Şirkət məlumatları"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class ServiceListView(generics.ListAPIView):
    """Aktiv xidmətlərin siyahısı"""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer


class TeamMemberListView(generics.ListAPIView):
    """Aktiv komanda üzvlərinin siyahısı"""
    queryset = TeamMember.objects.filter(is_active=True)
    serializer_class = TeamMemberSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['position']
    ordering_fields = ['order', 'full_name']
    ordering = ['order', 'full_name']


class FAQListView(generics.ListAPIView):
    """Aktiv FAQ-ların siyahısı"""
    queryset = FAQ.objects.filter(is_active=True)
    serializer_class = FAQSerializer


@api_view(['GET'])
def company_info(request):
    """Ana səhifə üçün şirkət məlumatları"""
    try:
        company = Company.objects.first()
        services = Service.objects.filter(is_active=True)[:4]  # İlk 4 xidmət
        team_members = TeamMember.objects.filter(is_active=True)[:3]  # İlk 3 komanda üzvü
        
        return Response({
            'company': CompanySerializer(company).data if company else None,
            'services': ServiceSerializer(services, many=True).data,
            'team_members': TeamMemberSerializer(team_members, many=True).data,
        })
    except Exception as e:
        return Response({'error': str(e)}, status=500)


def home_view(request):
    """Ana səhifə HTML view"""
    return render(request, 'home_simple.html')
