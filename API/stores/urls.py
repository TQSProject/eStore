from django.urls import path
from .views import StoreList, ProductList, StoreProductDetailAPIView, StoreProductListAPIView, StoreDetailAPIView

urlpatterns = [
    path('stores/', StoreList.as_view(), name='store-list'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('stores/<slug:slug>/', StoreDetailAPIView.as_view(), name='store-products-list'),
    path('stores/<slug:slug>/products/', StoreProductListAPIView.as_view(), name='store-products-list'),
    path('stores/<slug:slug>/products/<int:product_id>/', StoreProductDetailAPIView.as_view(), name='store-products-single'),
]