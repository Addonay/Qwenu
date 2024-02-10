from django.db import models
from oauth.models import User
# Create your models here.
class Rating(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=10, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rating