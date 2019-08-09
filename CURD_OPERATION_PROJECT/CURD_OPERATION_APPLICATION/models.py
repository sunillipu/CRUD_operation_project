from django.db import models

class ProductData(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    product_color=models.CharField(max_length=50)
    product_class=models.CharField(max_length=50)
    product_price=models.IntegerField()
    customer_name=models.CharField(max_length=50)
    customer_mobile=models.BigIntegerField()
    customer_email=models.EmailField(max_length=50)

