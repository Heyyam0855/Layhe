from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'E-poçtunuzu daxil edin',
            'id': 'email'
        })
    )
    ad = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Adınızı daxil edin',
            'id': 'name'
        })
    )
    soyad = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Soyadınızı daxil edin'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Şifrənizi daxil edin',
            'id': 'password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Şifrənizi təsdiqləyin',
            'id': 'passwordConfirm'
        })
    )

    class Meta:
        model = User
        fields = ['email', 'ad', 'soyad', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Email'i username kimi istifadə edirik
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            # Profili yeniləyirik
            profile = user.profile
            profile.ad = self.cleaned_data['ad']
            profile.soyad = self.cleaned_data.get('soyad', '')
            profile.save()
        
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'E-poçtunuzu daxil edin',
            'id': 'email'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-input',
            'placeholder': 'Şifrənizi daxil edin',
            'id': 'password'
        })
    )


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'E-poçt'
        })
    )

    class Meta:
        model = UserProfile
        fields = ['ad', 'soyad', 'telefon', 'unvan', 'dogum_tarixi']
        widgets = {
            'ad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Adınızı daxil edin'
            }),
            'soyad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Soyadınızı daxil edin'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+994'
            }),
            'unvan': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Ünvan'
            }),
            'dogum_tarixi': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields['email'].initial = self.user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        if self.user:
            self.user.email = self.cleaned_data['email']
            self.user.save()
        if commit:
            profile.save()
        return profile


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'E-poçtunuzu daxil edin',
            'id': 'email'
        })
    )
