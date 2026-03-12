from django.db import models


class Company(models.Model):
    """Şirkət məlumatları"""
    name = models.CharField(max_length=200, verbose_name="Şirkət adı")
    description = models.TextField(verbose_name="Təsvir")
    mission = models.TextField(verbose_name="Missiya", blank=True)
    vision = models.TextField(verbose_name="Vizyon", blank=True)
    address = models.TextField(verbose_name="Ünvan")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(verbose_name="E-mail")
    working_hours = models.CharField(max_length=100, verbose_name="İş saatları")
    logo = models.ImageField(upload_to='company/', verbose_name="Logo", blank=True)
    established_year = models.IntegerField(verbose_name="Təsis ili", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Şirkət"
        verbose_name_plural = "Şirkət məlumatları"
    
    def __str__(self):
        return self.name


class Service(models.Model):
    """Laboratoriya xidmətləri"""
    title = models.CharField(max_length=200, verbose_name="Xidmət adı")
    description = models.TextField(verbose_name="Təsvir")
    icon = models.CharField(max_length=50, verbose_name="Icon CSS class", 
                           help_text="FontAwesome icon class məsələn: fas fa-microscope")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Xidmət"
        verbose_name_plural = "Xidmətlər"
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class TeamMember(models.Model):
    """Komanda üzvləri"""
    POSITION_CHOICES = [
        ('doctor', 'Həkim'),
        ('lab_technician', 'Laborant'),
        ('manager', 'Menecer'),
        ('nurse', 'Tibb bacısı'),
        ('other', 'Digər'),
    ]
    
    full_name = models.CharField(max_length=200, verbose_name="Ad Soyad")
    position = models.CharField(max_length=20, choices=POSITION_CHOICES, verbose_name="Vəzifə")
    description = models.TextField(verbose_name="Təsvir", blank=True)
    photo = models.ImageField(upload_to='team/', verbose_name="Şəkil", blank=True)
    experience_years = models.IntegerField(verbose_name="Təcrübə (il)", blank=True, null=True)
    specialization = models.CharField(max_length=200, verbose_name="İxtisas", blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Komanda üzvü"
        verbose_name_plural = "Komanda üzvləri"
        ordering = ['order', 'full_name']
    
    def __str__(self):
        return f"{self.full_name} - {self.get_position_display()}"


class FAQ(models.Model):
    """Tez-tez verilən suallar"""
    question = models.CharField(max_length=300, verbose_name="Sual")
    answer = models.TextField(verbose_name="Cavab")
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıralama")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQ-lar"
        ordering = ['order', 'question']
    
    def __str__(self):
        return self.question[:50] + "..." if len(self.question) > 50 else self.question
