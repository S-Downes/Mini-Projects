from django.db import models
from products.models import Product

# Create your models here.
class Order(models.Model):
    """
    A Order model that stores attributes relating to user orders
    """
    full_name = models.CharField(max_length = 60, blank = False)
    phone_number = models.CharField(max_length= 50, blank = False)
    street_address1 = models.CharField(max_length = 40, blank = False)
    street_address2 = models.CharField(max_length = 40, blank = False)
    town_or_city = models.CharField(max_length = 40, blank = False)
    county = models.CharField(max_length = 40, blank = False)
    country = models.CharField(max_length = 40, blank = False)
    postcode = models.CharField(max_length = 20, blank = True)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
        
class OrderLineItem(models.Model):
    """
    Details of the product, quantity and price for each order created
    """
    order = models.ForeignKey(Order, null = False)
    product = models.ForeignKey(Product, null = False)
    quantity = models.IntegerField(blank = False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)
    