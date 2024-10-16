from django.urls import path
from Shops.views import CreateShopView, GetShopsView, CreateShopTemplate, GetShopTemplate


app_name = 'shop'

urlpatterns = [
    path('CreateShopAPI/', CreateShopView.as_view(), name='CreateShopAPI'),
    path('GetShopAPI/', GetShopsView.as_view(), name='GetShopAPI'),
    path('CreateShop/', CreateShopTemplate, name='CreateShop'),
    path('GetShop/', GetShopTemplate, name='GetShop'),
]