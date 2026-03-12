from django.urls import path
from . import views

app_name = 'tests'

urlpatterns = [
    path('categories/', views.TestCategoryListView.as_view(), name='category-list'),
    path('', views.TestListView.as_view(), name='test-list'),
    path('<int:pk>/', views.TestDetailView.as_view(), name='test-detail'),
    path('packages/', views.TestPackageListView.as_view(), name='package-list'),
    path('popular/', views.PopularTestsView.as_view(), name='popular-tests'),
    path('category/<str:category_type>/', views.tests_by_category, name='tests-by-category'),
    path('prices/', views.price_list, name='price-list'),
]