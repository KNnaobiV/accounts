from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser
from accounts.validators import validate_phone
# Create your models here.

class DefaultUser(AbstractUser):
    "fdg"
    phone = models.PositiveIntegerField(
        null=True, blank=True, validators=[validate_phone] 
    )
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('accounts:profile', kwargs={
         'pk': self.pk, 'username': self.username,
        })

     