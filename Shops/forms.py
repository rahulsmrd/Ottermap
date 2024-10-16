# from django import forms
# from Shops.models import shop

# class ShopForm(forms.ModelForm):
#     class Meat:
#         model = shop
#         fields = [
#             'shop_name', 
#             'shop_description',
#             'shop_latitude',
#             'shop_longitude',
#             'shop_city',
#             'shop_state',
#         ]
#         widgets = {
#             'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'shop_description': forms.Textarea(attrs={'class': 'form-control'}),
#             'shop_latitude': forms.FloatField(attrs={'class': 'form-control'}),
#             'shop_longitude': forms.FloatField(attrs={'class': 'form-control'}),
#             'shop_city': forms.TextInput(attrs={'class': 'form-control'}),
#             'shop_state': forms.TextInput(attrs={'class': 'form-control'}),
#         }