from django.db import models

# Create your models here.
class CartItem(models. Model):
    # id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length =255)
    # price = models.FloatField()
    # quantity = models.IntegerField()
    product_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.IntegerField(default=1)
    discription = models.CharField(max_length = 200)
    image =models.CharField(max_length =2000)
    def subtotal(self):
        return self.product_price * self.quantity