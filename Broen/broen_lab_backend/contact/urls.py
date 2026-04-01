from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('message/', views.ContactMessageCreateView.as_view(), name='message-create'),
    path('newsletter/', views.NewsletterSubscriptionCreateView.as_view(), name='newsletter-subscribe'),
    path('info/', views.ContactInfoListView.as_view(), name='contact-info'),
    path('social/', views.SocialMediaListView.as_view(), name='social-media'),
    path('form-submit/', views.contact_form_submit, name='form-submit'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter-subscribe-form'),
    path('page-data/', views.contact_page_data, name='page-data'),
]