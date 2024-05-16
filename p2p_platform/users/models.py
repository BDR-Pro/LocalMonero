from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    rating = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    num_of_deals = models.IntegerField(default=0)
    num_of_buys = models.IntegerField(default=0)
    # Rename the reviews ManyToManyField to avoid conflict
    review_set = models.ManyToManyField('Review', related_name='reviewed_users', blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='written_reviews')
    text = models.TextField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.author} -> {self.user}'
