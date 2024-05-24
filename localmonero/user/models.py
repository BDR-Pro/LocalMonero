from django.db import models
from django.contrib.auth.models import User
from web.utils.btc import check_balance_by_address as get_balance_btc , get_new_address as get_btc_address
from web.utils.Monero import check_balance_by_address as get_balance_xmr , create_address as get_xmr_address
# Create your models here.
class Profile(models.Model):
    """
    Profile model

    Args:
        model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, default="Making the world a better place.")
    location = models.CharField(max_length=30, default="Mars")
    btc_address = models.CharField(max_length=34, default="")
    xmr_address = models.CharField(max_length=95, default="")
    localmarket_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    btc_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    xmr_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        """
        save method

        Args:
            self
        """
        if not self.btc_address:
            self.btc_address = get_btc_address()
        if not self.xmr_address:
            self.xmr_address = get_xmr_address()
        super(Profile, self).save(*args, **kwargs)
        
    
    
    
    def calculate_xmr_balance(self):
        """
        calculate xmr balance

        Args:
            self

        Returns:
            xmr_balance
        """
        if not self.xmr_address:
            self.xmr_address = get_xmr_address()
            self.save()

        xmr_balance = get_balance_xmr(self.xmr_address)
        self.xmr_balance = xmr_balance
        self.save()
        return xmr_balance
    
    def calculate_btc_balance(self):
        """
        calculate btc balance

        Args:
            self

        Returns:
            btc_balance
        """
        btc_balance = get_balance_btc(self.btc_address)
        self.btc_balance = btc_balance
        self.save()
        return btc_balance
    
