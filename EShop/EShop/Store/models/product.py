from django.db import models
from .category import Category

class product(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='upload/products/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
