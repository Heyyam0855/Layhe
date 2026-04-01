from django.db import models


class ContactMessage(models.Model):
    """Əlaqə formu mesajları"""
    STATUS_CHOICES = [
        ('new', 'Yeni'),
        ('in_progress', 'Baxılır'),
        ('resolved', 'Həll edilib'),
        ('closed', 'Bağlanıb'),
    ]
    
    # Əsas məlumatlar
    first_name = models.CharField(max_length=100, verbose_name="Ad")
    last_name = models.CharField(max_length=100, verbose_name="Soyad")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-mail")
    
    # Əlavə məlumatlar
    subject = models.CharField(max_length=200, verbose_name="Mövzu", blank=True)
    test_type = models.CharField(max_length=100, verbose_name="Test növü", blank=True)
    preferred_date = models.DateField(verbose_name="Üstünlük verilən tarix", blank=True, null=True)
    message = models.TextField(verbose_name="Mesaj")
    
    # Status və idarəetmə
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, 
                            default='new', verbose_name="Status")
    admin_notes = models.TextField(verbose_name="Admin qeydləri", blank=True)
    is_urgent = models.BooleanField(default=False, verbose_name="Təcili")
    is_responded = models.BooleanField(default=False, verbose_name="Cavablandırılıb")
    
    # Tarix məlumatları
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaradılma tarixi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yenilənmə tarixi")
    responded_at = models.DateTimeField(verbose_name="Cavab tarixi", blank=True, null=True)
    
    class Meta:
        verbose_name = "Əlaqə Mesajı"
        verbose_name_plural = "Əlaqə Mesajları"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject or 'Mesaj'}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class NewsletterSubscription(models.Model):
    """Newsletter abunəliyi"""
    email = models.EmailField(unique=True, verbose_name="E-mail")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    subscribed_at = models.DateTimeField(auto_now_add=True, verbose_name="Abunə olma tarixi")
    unsubscribed_at = models.DateTimeField(verbose_name="Abunəlikdən çıxma tarixi", 
                                         blank=True, null=True)
    
    class Meta:
        verbose_name = "Newsletter Abunəliyi"
        verbose_name_plural = "Newsletter Abunəlikləri"
        ordering = ['-subscribed_at']
    
    def __str__(self):
        return f"{self.email} - {'Aktiv' if self.is_active else 'Deaktiv'}"


class ContactInfo(models.Model):
    """Əlaqə məlumatları"""
    name = models.CharField(max_length=100, verbose_name="Məlumat adı")
    value = models.TextField(verbose_name="Dəyər")
    icon = models.CharField(max_length=50, verbose_name="Icon CSS class", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Əlaqə Məlumatı"
        verbose_name_plural = "Əlaqə Məlumatları"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name}: {self.value}"


class SocialMedia(models.Model):
    """Sosial media hesabları"""
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('whatsapp', 'WhatsApp'),
        ('linkedin', 'LinkedIn'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter'),
        ('telegram', 'Telegram'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, 
                               verbose_name="Platform")
    username = models.CharField(max_length=100, verbose_name="İstifadəçi adı")
    url = models.URLField(verbose_name="URL")
    icon = models.CharField(max_length=50, verbose_name="Icon CSS class")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Sosial Media"
        verbose_name_plural = "Sosial Media Hesabları"
        ordering = ['order', 'platform']
    
    def __str__(self):
        return f"{self.get_platform_display()} - @{self.username}"
