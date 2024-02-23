from django.urls import path
from .views import HomePageView, AboutPageView,ProductIndexView, ProductShowView, ProductCreateView, ContactPageView, CreatedPageView, CartView, CartRemoveAllView

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('products/', ProductIndexView.as_view(), name='index'),
    path('products/create', ProductCreateView.as_view(), name='form'),
    path('products/<str:id>', ProductShowView.as_view(), name='show'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('products/create/success/', CreatedPageView.as_view(), name='product_create_success'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),



]
