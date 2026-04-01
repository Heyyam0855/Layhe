from rest_framework import serializers
from .models import TestCategory, Test, TestPackage


class TestCategorySerializer(serializers.ModelSerializer):
    test_count = serializers.SerializerMethodField()
    
    class Meta:
        model = TestCategory
        fields = '__all__'
    
    def get_test_count(self, obj):
        return obj.tests.filter(is_active=True).count()


class TestSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_type = serializers.CharField(source='category.category_type', read_only=True)
    effective_price = serializers.ReadOnlyField()
    has_discount = serializers.ReadOnlyField()
    
    class Meta:
        model = Test
        fields = '__all__'


class TestListSerializer(serializers.ModelSerializer):
    """Test siyahısı üçün sadələşdirilmiş serializer"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_type = serializers.CharField(source='category.category_type', read_only=True)
    effective_price = serializers.ReadOnlyField()
    has_discount = serializers.ReadOnlyField()
    
    class Meta:
        model = Test
        fields = ['id', 'name', 'code', 'category_name', 'category_type', 
                 'price', 'discount_price', 'effective_price', 'has_discount',
                 'is_popular', 'result_time', 'sample_type']


class TestPackageSerializer(serializers.ModelSerializer):
    tests = TestListSerializer(many=True, read_only=True)
    test_count = serializers.SerializerMethodField()
    individual_total_price = serializers.ReadOnlyField()
    savings_amount = serializers.ReadOnlyField()
    
    class Meta:
        model = TestPackage
        fields = '__all__'
    
    def get_test_count(self, obj):
        return obj.tests.count()


class TestPriceSerializer(serializers.ModelSerializer):
    """Qiymət səhifəsi üçün minimal test məlumatları"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_type = serializers.CharField(source='category.category_type', read_only=True)
    effective_price = serializers.ReadOnlyField()
    has_discount = serializers.ReadOnlyField()
    
    class Meta:
        model = Test
        fields = ['id', 'name', 'code', 'category_name', 'category_type', 
                 'price', 'discount_price', 'effective_price', 'has_discount', 'result_time']