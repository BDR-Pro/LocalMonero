from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    num_of_deals = models.IntegerField(default=0)
    num_of_buys = models.IntegerField(default=0)
    Reviews = models.ManyToManyField('Review', related_name='reviews', blank=True)
    
    
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='written_reviews')
    text = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} -> {self.user}'