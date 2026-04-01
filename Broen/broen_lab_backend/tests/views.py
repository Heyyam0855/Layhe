from rest_framework import generics, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import TestCategory, Test, TestPackage
from .serializers import (TestCategorySerializer, TestSerializer, TestListSerializer, 
                         TestPackageSerializer, TestPriceSerializer)


class TestCategoryListView(generics.ListAPIView):
    """Test kateqoriyalarının siyahısı"""
    queryset = TestCategory.objects.filter(is_active=True)
    serializer_class = TestCategorySerializer


class TestListView(generics.ListAPIView):
    """Testlərin siyahısı"""
    queryset = Test.objects.filter(is_active=True)
    serializer_class = TestListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__category_type', 'is_popular']
    search_fields = ['name', 'code', 'description']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['category', 'order', 'name']


class TestDetailView(generics.RetrieveAPIView):
    """Test təfərrüatları"""
    queryset = Test.objects.filter(is_active=True)
    serializer_class = TestSerializer


class TestPackageListView(generics.ListAPIView):
    """Test paketlərinin siyahısı"""
    queryset = TestPackage.objects.filter(is_active=True)
    serializer_class = TestPackageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'package_price']
    ordering = ['order', 'name']


class PopularTestsView(generics.ListAPIView):
    """Məşhur testlər"""
    queryset = Test.objects.filter(is_active=True, is_popular=True)
    serializer_class = TestListSerializer


@api_view(['GET'])
def tests_by_category(request, category_type):
    """Kateqoriyaya görə testlər"""
    try:
        category = TestCategory.objects.get(category_type=category_type, is_active=True)
        tests = Test.objects.filter(category=category, is_active=True)
        
        return Response({
            'category': TestCategorySerializer(category).data,
            'tests': TestPriceSerializer(tests, many=True).data,
        })
    except TestCategory.DoesNotExist:
        return Response({'error': 'Kateqoriya tapılmadı'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['GET'])
def price_list(request):
    """Qiymət cədvəli"""
    try:
        categories = TestCategory.objects.filter(is_active=True)
        result = []
        
        for category in categories:
            tests = Test.objects.filter(category=category, is_active=True)
            result.append({
                'category': TestCategorySerializer(category).data,
                'tests': TestPriceSerializer(tests, many=True).data,
            })
        
        return Response(result)
    except Exception as e:
        return Response({'error': str(e)}, status=500)
