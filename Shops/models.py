from django.db import models

# Create your models here.
class shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_description = models.TextField()
    shop_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    shop_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    shop_city = models.CharField(max_length=100)
    shop_state = models.CharField(max_length=100)
    distance = models.PositiveIntegerField(default=0)
    
    def __str__(self) -> str:
        return self.shop_name + '-' + self.shop_city