from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, PasswordResetRequestForm
from .models import UserProfile


def index_view(request):
    """Ana səhifə"""
    return render(request, 'accounts/index.html')


def register_view(request):
    """İstifadəçi qeydiyyatı"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Qeydiyyat uğurla tamamlandı! İndi daxil ola bilərsiniz.')
            login(request, user)
            return redirect('index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UserRegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """İstifadəçi girişi"""
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        
        # Email ilə istifadəçi tapırıq
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            
            if user is not None:
                login(request, user)
                remember_me = request.POST.get('remember_me')
                if not remember_me:
                    request.session.set_expiry(0)
                messages.success(request, f'Xoş gəldiniz, {user.profile.ad}!')
                return redirect('index')
            else:
                messages.error(request, 'E-poçt və ya şifrə yanlışdır!')
        except User.DoesNotExist:
            messages.error(request, 'Bu e-poçt ünvanı ilə istifadəçi tapılmadı!')
    
    form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """İstifadəçi çıxışı"""
    logout(request)
    messages.success(request, 'Uğurla çıxış etdiniz!')
    return redirect('login')


@login_required
def profile_view(request):
    """İstifadəçi profili"""
    profile = request.user.profile
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil məlumatları yeniləndi!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile, user=request.user)
    
    return render(request, 'accounts/profile.html', {'form': form, 'profile': profile})


@login_required
def admin_panel_view(request):
    """Admin paneli - bütün istifadəçilərin siyahısı"""
    if not request.user.is_staff:
        messages.error(request, 'Bu səhifəyə giriş icazəniz yoxdur!')
        return redirect('index')
    
    users = UserProfile.objects.all()
    
    # Axtarış funksiyası
    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            ad__icontains=search_query
        ) | users.filter(
            soyad__icontains=search_query
        ) | users.filter(
            user__email__icontains=search_query
        )
    
    context = {
        'users': users,
        'search_query': search_query,
        'total_users': UserProfile.objects.count()
    }
    return render(request, 'accounts/admin_panel.html', context)


def forgot_password_view(request):
    """Şifrə bərpası"""
    if request.method == 'POST':
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                # Burada email göndərmə funksiyası əlavə edilə bilər
                messages.success(request, 'Şifrə bərpası linki e-poçtunuza göndərildi!')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, 'Bu e-poçt ünvanı ilə istifadəçi tapılmadı!')
    else:
        form = PasswordResetRequestForm()
    
    return render(request, 'accounts/forgot_password.html', {'form': form})


def data_file_view(request):
    """data.txt faylını oxuyur və göstərir"""
    content = ""
    try:
        with open('data.txt', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        content = "Fayl tapılmadı və ya heç bir məlumat əlavə edilməyib."
    
    return render(request, 'accounts/data_file.html', {'content': content})
