"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from store import views
from store.views import ProductListCreateViewSet, ProductRetrieveUpdateDestroyAPIViewSet

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'suppliers', views.SupplierViewSet, basename='supplier')
router.register(r'addresses', views.AddressViewSet, basename='address')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('products/', ProductListCreateViewSet.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIViewSet.as_view(), name='product-detail'),
    path('product-details/', views.ProductDetailListCreateViewSet.as_view(), name='product-detail'),
    path('product-details/<int:pk>/',
         views.ProductDetailRetrieveUpdateDeleteView.as_view(), name='product-detail-update'),
    path('customers/', views.CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailUpdateDeleteView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token'),


]
