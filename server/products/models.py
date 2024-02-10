from django.db import models
from category.models import Category
from reviews.models import Rating
import secrets

# Create your models here.
class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=255, default=secrets.token_hex(12),editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
