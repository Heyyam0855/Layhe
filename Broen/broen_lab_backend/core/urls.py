from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('company/', views.CompanyListView.as_view(), name='company-list'),
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('team/', views.TeamMemberListView.as_view(), name='team-list'),
    path('faq/', views.FAQListView.as_view(), name='faq-list'),
    path('company-info/', views.company_info, name='company-info'),
]