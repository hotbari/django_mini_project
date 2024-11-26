from django.db import models
from users.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=30)
    bank_code = models.CharField(max_length=10)
    account_type = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.account_number} ({self.bank_code})"

# Create your models here.
