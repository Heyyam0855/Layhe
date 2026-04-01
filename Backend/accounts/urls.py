from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('admin-panel/', views.admin_panel_view, name='admin_panel'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('data-file/', views.data_file_view, name='data_file'),
]
