"""
URL configuration for broen_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import home_view
from core.test_views import test_view

urlpatterns = [
    # Root URL - Homepage
    path('', home_view, name='home'),
    
    # Test page
    path('test/', test_view, name='test'),
    
    path('admin/', admin.site.urls),
    
    # API endpoints
    path('api/core/', include('core.urls')),
    path('api/tests/', include('tests.urls')),
    path('api/contact/', include('contact.urls')),
]

# Static və media fayllar üçün
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
