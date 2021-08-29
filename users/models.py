from django.db import models
from django.utils import timezone
from django.utils.translation import getting_lazy as _
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class NewUser(AbstractBaseUser):
    email = models.EmailField(_('email address'),unique=True)
    user_name = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'),max_length=500,blank=True)
    is_staff =models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
