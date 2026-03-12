from django.db import models


class TestCategory(models.Model):
    """Test kateqoriyaları"""
    CATEGORY_TYPES = [
        ('blood', 'Qan Analizləri'),
        ('hormone', 'Hormon Testləri'),
        ('infection', 'İnfeksiya Testləri'),
        ('allergy', 'Allergodiaqnostika'),
        ('biochemistry', 'Biokimya'),
        ('immunology', 'İmmunologiya'),
        ('other', 'Digər'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Kateqoriya adı")
    category_type = models.CharField(max_length=15, choices=CATEGORY_TYPES, 
                                   verbose_name="Kateqoriya tipi", unique=True)
    description = models.TextField(verbose_name="Təsvir", blank=True)
    icon = models.CharField(max_length=50, verbose_name="Icon CSS class", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Test Kateqoriyası"
        verbose_name_plural = "Test Kateqoriyaları"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Test(models.Model):
    """Laboratoriya testləri"""
    name = models.CharField(max_length=200, verbose_name="Test adı")
    category = models.ForeignKey(TestCategory, on_delete=models.CASCADE, 
                               verbose_name="Kateqoriya", related_name="tests")
    code = models.CharField(max_length=20, verbose_name="Test kodu", unique=True)
    description = models.TextField(verbose_name="Təsvir", blank=True)
    preparation_info = models.TextField(verbose_name="Hazırlıq məlumatları", blank=True,
                                      help_text="Test öncəsi hazırlıq göstərişləri")
    sample_type = models.CharField(max_length=100, verbose_name="Nümunə növü", 
                                 help_text="Qan, sidik, ağız suyu və s.")
    result_time = models.CharField(max_length=50, verbose_name="Nəticə müddəti",
                                 help_text="Məsələn: 1-2 iş günü")
    normal_range = models.TextField(verbose_name="Normal dəyərlər", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Qiymət (AZN)")
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, 
                                       verbose_name="Endirimli qiymət (AZN)", 
                                       blank=True, null=True)
    is_popular = models.BooleanField(default=False, verbose_name="Məşhur test")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlər"
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.code})"
    
    @property
    def effective_price(self):
        """Endirimli qiymət varsa onu, yoxsa əsas qiyməti qaytarır"""
        return self.discount_price if self.discount_price else self.price
    
    @property
    def has_discount(self):
        """Endirimin olub-olmadığını yoxlayır"""
        return self.discount_price is not None and self.discount_price < self.price


class TestPackage(models.Model):
    """Test paketləri"""
    name = models.CharField(max_length=200, verbose_name="Paket adı")
    description = models.TextField(verbose_name="Təsvir")
    tests = models.ManyToManyField(Test, verbose_name="Testlər", related_name="packages")
    package_price = models.DecimalField(max_digits=10, decimal_places=2, 
                                      verbose_name="Paket qiyməti (AZN)")
    discount_percentage = models.IntegerField(verbose_name="Endirim faizi", 
                                            help_text="Fərdi qiymətlərdən nə qədər endirim")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    is_featured = models.BooleanField(default=False, verbose_name="Öne çıxarılmış")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Test Paketi"
        verbose_name_plural = "Test Paketləri"
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name
    
    @property
    def individual_total_price(self):
        """Testlərin fərdi qiymətlərinin cəmi"""
        return sum(test.effective_price for test in self.tests.all())
    
    @property
    def savings_amount(self):
        """Paket alarkən nə qədər qənaət edilir"""
        return self.individual_total_price - self.package_price
