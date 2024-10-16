from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status
from rest_framework.response import Response
import requests

from Shops.Haversine import haversine
from Shops.serializers import ShopSerializer
from Shops.models import shop
# from Shops.forms import ShopForm

# Create your views here.

def home(request):
    return render(request, 'Shops/home.html')
def CreateShopTemplate(request):
    if request.method == 'POST':

        url = 'http://127.0.0.1:8000/shops/v1/CreateShopAPI/'
        data = {
            'shop_name' : request.POST.get('Name'),
            'shop_description': request.POST.get('Description'),
            'shop_latitude': float(request.POST.get('Latitude')),
            'shop_longitude': float(request.POST.get('Longitude')),
            'shop_city' : request.POST.get('City'),
            'shop_state': request.POST.get('State'),
        }
        response = requests.post(url, json=data)
        if response.status_code == 201:
            return render(request, 'Shops/createShop.html', {'response': response, 'status': status.HTTP_201_CREATED})
        else:
            return render(request, 'Shops/createShop.html', {'response': response.text, 'status': status.HTTP_404_NOT_FOUND})
    return render(request, 'Shops/createShop.html')

def GetShopTemplate(request):
    if request.method == 'GET':
        url = 'http://127.0.0.1:8000/shops/v1/GetShopAPI/'
        data = {
            'lat': request.GET.get('lat'),
            'long': request.GET.get('long')
        }
        response = requests.get(url, params=data)
        print(response)
        if response.status_code == 200:
            return render(request, 'Shops/getShop.html', {'shops': response.json(), 'status': status.HTTP_200_OK, 'lat':data['lat'], 'long':data['long']})
        else:
            return render(request, 'Shops/getShop.html', {'shops': response.json(), 'status': status.HTTP_404_NOT_FOUND})
    return render(request, 'Shops/getShop.html')
#<------------ APIs ---------------------->
class CreateShopView(CreateAPIView):
    serializer_class = ShopSerializer
    queryset = shop.objects.all()

class GetShopsView(ListAPIView):
    serializer_class = ShopSerializer
    queryset = shop.objects.all().order_by('distance')
    def get(self, request, *args, **kwargs):
        try:
            lat1 = float(request.GET.get('lat'))
            long1 = float(request.GET.get('long'))
            print(lat1, long1)
        except TypeError as e:
            return Response({"Error" : "Latitude and Longitude must be given"}, status=status.HTTP_404_NOT_FOUND)
        queryset = self.get_queryset()
        for query in queryset:
            distance = haversine(lat1, long1, query.shop_latitude, query.shop_longitude)
            query.distance = distance
            query.save()
        return super().get(request, *args, **kwargs)