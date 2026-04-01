from django.core.management.base import BaseCommand
from core.models import Company, Service, FAQ, TeamMember
from tests.models import TestCategory, Test, TestPackage
from contact.models import ContactInfo, SocialMedia


class Command(BaseCommand):
    help = 'Başlanğıc məlumatları yükləyir (seed data)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Başlanğıc məlumatları yüklənir...'))

        # Şirkət məlumatları
        self.create_company_data()
        
        # Xidmətlər
        self.create_services()
        
        # FAQ-lar
        self.create_faqs()
        
        # Komanda üzvləri
        self.create_team_members()
        
        # Test kateqoriyaları
        self.create_test_categories()
        
        # Testlər
        self.create_tests()
        
        # Test paketləri
        self.create_test_packages()
        
        # Əlaqə məlumatları
        self.create_contact_info()
        
        # Sosial media
        self.create_social_media()

        self.stdout.write(self.style.SUCCESS('Başlanğıc məlumatları uğurla yükləndi!'))

    def create_company_data(self):
        Company.objects.get_or_create(
            name='BRO-EN Laboratoriya',
            defaults={
                'description': 'Bakının ən etibarlı tibbi laboratoriyası. Yüksək keyfiyyətli analiz xidmətləri, müasir avadanlıq və peşəkar komanda ilə sağlamlığınıza qulluq edirik.',
                'mission': 'Müasir texnologiyalar və peşəkar yanaşma ilə ən yüksək keyfiyyətli laboratoriya xidmətlərini təqdim etmək',
                'vision': 'Azərbaycanda tibbi laboratoriya xidmətləri sahəsində lider olmaq',
                'address': 'Bakı şəhəri, Nəsimi rayonu, Azadlıq prospekti 15',
                'phone': '+994 12 555-55-55',
                'email': 'info@broen.az',
                'working_hours': 'Bazar ertəsi - Şənbə: 09:00 - 18:00',
                'established_year': 2015,
            }
        )
        self.stdout.write('✓ Şirkət məlumatları yaradıldı')

    def create_services(self):
        services = [
            {
                'title': 'Sürətli Nəticə',
                'description': 'Testlərin nəticələri 1-3 iş günü ərzində hazır olur',
                'icon': 'fas fa-clock',
                'order': 1
            },
            {
                'title': 'Keyfiyyət Təminatı',
                'description': 'ISO sertifikatı və beynəlxalq standartlara uyğun xidmət',
                'icon': 'fas fa-shield-alt',
                'order': 2
            },
            {
                'title': 'Peşəkar Komanda',
                'description': 'Təcrübəli həkimlər və laborant specialistlər',
                'icon': 'fas fa-user-md',
                'order': 3
            },
            {
                'title': 'Müasir Avadanlıq',
                'description': 'Ən son texnologiyalar və avadanlıqlar',
                'icon': 'fas fa-laptop-medical',
                'order': 4
            },
        ]
        
        for service_data in services:
            Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
        self.stdout.write('✓ Xidmətlər yaradıldı')

    def create_faqs(self):
        faqs = [
            {
                'question': 'Test nəticələri nə qədər müddətdə hazır olur?',
                'answer': 'Test nəticələri adətən 1-3 iş günü ərzində hazır olur. Təcili hallar üçün 24 saat ərzində nəticə əldə etmək mümkündür.',
                'order': 1
            },
            {
                'question': 'Testlər üçün əvvəlcədən randevu almalıyammı?',
                'answer': 'Xeyr, əvvəlcədən randevu almaq məcburi deyil. Ancaq gözləmə müddətini azaltmaq üçün öncədən əlaqə saxlamağınız tövsiyə olunur.',
                'order': 2
            },
            {
                'question': 'Test öncəsi hansı hazırlıqlar aparılmalıdır?',
                'answer': 'Əksər qan testləri üçün 8-12 saat aclıq tələb olunur. Hər test üçün xüsusi hazırlıq göstərişləri test məlumatlarında qeyd olunur.',
                'order': 3
            },
        ]
        
        for faq_data in faqs:
            FAQ.objects.get_or_create(
                question=faq_data['question'],
                defaults=faq_data
            )
        self.stdout.write('✓ FAQ-lar yaradıldı')

    def create_team_members(self):
        team_members = [
            {
                'full_name': 'Dr. Aynur Məmmədova',
                'position': 'doctor',
                'description': 'Laboratoriya sahəsində 15 illik təcrübəyə malik baş həkim',
                'experience_years': 15,
                'specialization': 'Klinik laboratoriya diagnostikası',
                'is_active': True,
                'order': 1
            },
            {
                'full_name': 'Günel Əliyeva',
                'position': 'lab_technician',
                'description': 'Peşəkar laborant, qan analizləri üzrə mütəxəssis',
                'experience_years': 8,
                'specialization': 'Qan analizləri',
                'is_active': True,
                'order': 2
            },
            {
                'full_name': 'Rəşad Həsənov',
                'position': 'manager',
                'description': 'Laboratoriya əməliyyatları üzrə menecer',
                'experience_years': 5,
                'specialization': 'Keyfiyyət menecmenti',
                'is_active': True,
                'order': 3
            },
        ]
        
        for member_data in team_members:
            TeamMember.objects.get_or_create(
                full_name=member_data['full_name'],
                defaults=member_data
            )
        self.stdout.write('✓ Komanda üzvləri yaradıldı')

    def create_test_categories(self):
        categories = [
            {'name': 'Qan Analizləri', 'category_type': 'blood', 'icon': 'fas fa-tint', 'order': 1},
            {'name': 'Hormon Testləri', 'category_type': 'hormone', 'icon': 'fas fa-heartbeat', 'order': 2},
            {'name': 'İnfeksiya Testləri', 'category_type': 'infection', 'icon': 'fas fa-virus', 'order': 3},
            {'name': 'Allergodiaqnostika', 'category_type': 'allergy', 'icon': 'fas fa-allergies', 'order': 4},
        ]
        
        for cat_data in categories:
            TestCategory.objects.get_or_create(
                category_type=cat_data['category_type'],
                defaults=cat_data
            )
        self.stdout.write('✓ Test kateqoriyaları yaradıldı')

    def create_tests(self):
        blood_cat = TestCategory.objects.get(category_type='blood')
        hormone_cat = TestCategory.objects.get(category_type='hormone')
        infection_cat = TestCategory.objects.get(category_type='infection')
        allergy_cat = TestCategory.objects.get(category_type='allergy')
        
        tests = [
            # Qan analizləri
            {
                'name': 'Ümumi Qan Analizi',
                'code': 'QAN001',
                'category': blood_cat,
                'description': 'Qanda hüceyrələrin sayının və strukturunun yoxlanılması',
                'sample_type': 'Kapillyar və ya venoz qan',
                'result_time': '1 iş günü',
                'price': 15.00,
                'is_popular': True,
                'order': 1
            },
            {
                'name': 'Biokimyəvi Qan Analizi',
                'code': 'QAN002',
                'category': blood_cat,
                'description': 'Qanda kimyəvi maddələrin səviyyəsinin ölçülməsi',
                'sample_type': 'Venoz qan',
                'result_time': '1-2 iş günü',
                'price': 25.00,
                'discount_price': 20.00,
                'is_popular': True,
                'order': 2
            },
            {
                'name': 'Qan Qrupu və Rezus',
                'code': 'QAN003',
                'category': blood_cat,
                'description': 'Qan qrupunun və rezus faktorunun təyini',
                'sample_type': 'Venoz qan',
                'result_time': '1 iş günü',
                'price': 10.00,
                'order': 3
            },
            
            # Hormon testləri
            {
                'name': 'Qalxanabənzər Vəzi Hormonları (T3, T4, TSH)',
                'code': 'HOR001',
                'category': hormone_cat,
                'description': 'Qalxanabənzər vəzi fəaliyyətinin qiymətləndirilməsi',
                'sample_type': 'Venoz qan',
                'result_time': '2 iş günü',
                'price': 30.00,
                'is_popular': True,
                'order': 1
            },
            {
                'name': 'Cinsiyyət Hormonları',
                'code': 'HOR002',
                'category': hormone_cat,
                'description': 'Testosteron, estrogen və digər cinsiyyət hormonlarının ölçülməsi',
                'sample_type': 'Venoz qan',
                'result_time': '2-3 iş günü',
                'price': 35.00,
                'discount_price': 30.00,
                'order': 2
            },
            
            # İnfeksiya testləri
            {
                'name': 'Hepatit Markerleri (A, B, C)',
                'code': 'INF001',
                'category': infection_cat,
                'description': 'Hepatit viruslarının yoxlanılması',
                'sample_type': 'Venoz qan',
                'result_time': '2 iş günü',
                'price': 40.00,
                'is_popular': True,
                'order': 1
            },
            {
                'name': 'HIV Test',
                'code': 'INF002',
                'category': infection_cat,
                'description': 'HIV infeksiyasının yoxlanılması',
                'sample_type': 'Venoz qan',
                'result_time': '2 iş günü',
                'price': 20.00,
                'order': 2
            },
            
            # Allergiya testləri
            {
                'name': 'Allergen Panel (Qida)',
                'code': 'ALG001',
                'category': allergy_cat,
                'description': 'Qida məhsullarına allergiya testləri',
                'sample_type': 'Venoz qan',
                'result_time': '3 iş günü',
                'price': 50.00,
                'discount_price': 45.00,
                'order': 1
            },
            {
                'name': 'Allergen Panel (İnhalasiya)',
                'code': 'ALG002',
                'category': allergy_cat,
                'description': 'Tənəffüs yolu allergenlərinin testləri',
                'sample_type': 'Venoz qan',
                'result_time': '3 iş günü',
                'price': 50.00,
                'order': 2
            },
        ]
        
        for test_data in tests:
            Test.objects.get_or_create(
                code=test_data['code'],
                defaults=test_data
            )
        self.stdout.write('✓ Testlər yaradıldı')

    def create_test_packages(self):
        package_data = {
            'name': 'Kompleks Sağlamlıq Paketi',
            'description': 'Ümumi sağlamlıq vəziyyətinin qiymətləndirilməsi üçün əsas testlər paketi',
            'package_price': 80.00,
            'discount_percentage': 20,
            'is_featured': True,
            'order': 1
        }
        
        package, created = TestPackage.objects.get_or_create(
            name=package_data['name'],
            defaults=package_data
        )
        
        if created:
            tests = Test.objects.filter(code__in=['QAN001', 'QAN002', 'HOR001'])
            package.tests.set(tests)
            
        self.stdout.write('✓ Test paketləri yaradıldı')

    def create_contact_info(self):
        contact_info = [
            {'name': 'Telefon', 'value': '+994 12 555-55-55', 'icon': 'fas fa-phone', 'order': 1},
            {'name': 'Email', 'value': 'info@broen.az', 'icon': 'fas fa-envelope', 'order': 2},
            {'name': 'Ünvan', 'value': 'Bakı şəhəri, Nəsimi rayonu, Azadlıq prospekti 15', 'icon': 'fas fa-map-marker-alt', 'order': 3},
            {'name': 'İş saatları', 'value': 'Bazar ertəsi - Şənbə: 09:00 - 18:00', 'icon': 'fas fa-clock', 'order': 4},
        ]
        
        for info_data in contact_info:
            ContactInfo.objects.get_or_create(
                name=info_data['name'],
                defaults=info_data
            )
        self.stdout.write('✓ Əlaqə məlumatları yaradıldı')

    def create_social_media(self):
        social_media = [
            {
                'platform': 'facebook',
                'username': 'broenlaboratory',
                'url': 'https://facebook.com/broenlaboratory',
                'icon': 'fab fa-facebook',
                'order': 1
            },
            {
                'platform': 'instagram',
                'username': 'broen_lab',
                'url': 'https://instagram.com/broen_lab',
                'icon': 'fab fa-instagram',
                'order': 2
            },
            {
                'platform': 'whatsapp',
                'username': '+994505555555',
                'url': 'https://wa.me/994505555555',
                'icon': 'fab fa-whatsapp',
                'order': 3
            },
        ]
        
        for social_data in social_media:
            SocialMedia.objects.get_or_create(
                platform=social_data['platform'],
                defaults=social_data
            )
        self.stdout.write('✓ Sosial media hesabları yaradıldı')