from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ad = models.CharField(max_length=100, verbose_name="Ad")
    soyad = models.CharField(max_length=100, verbose_name="Soyad")
    telefon = models.CharField(max_length=20, blank=True, verbose_name="Telefon")
    unvan = models.TextField(blank=True, verbose_name="Ünvan")
    dogum_tarixi = models.DateField(null=True, blank=True, verbose_name="Doğum Tarixi")
    qeyd_tarixi = models.DateTimeField(auto_now_add=True, verbose_name="Qeydiyyat Tarixi")
    yenileme_tarixi = models.DateTimeField(auto_now=True, verbose_name="Yeniləmə Tarixi")

    class Meta:
        verbose_name = "İstifadəçi Profili"
        verbose_name_plural = "İstifadəçi Profilləri"
        ordering = ['-qeyd_tarixi']

    def __str__(self):
        return f"{self.ad} {self.soyad}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # data.txt faylına məlumatları yaz
        self.save_to_file()

    def save_to_file(self):
        """Məlumatları data.txt faylına yazır"""
        try:
            with open('data.txt', 'a', encoding='utf-8') as f:
                f.write(f"Ad: {self.ad}\n")
                f.write(f"Soyad: {self.soyad}\n")
                f.write(f"Email: {self.user.email}\n")
                f.write(f"Telefon: {self.telefon}\n")
                f.write(f"Ünvan: {self.unvan}\n")
                f.write(f"Qeydiyyat Tarixi: {self.qeyd_tarixi}\n")
                f.write("-" * 50 + "\n")
        except Exception as e:
            print(f"Fayla yazma xətası: {e}")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Yeni user yaradıldıqda avtomatik profil yaradır"""
    if created:
        UserProfile.objects.create(user=instance)
