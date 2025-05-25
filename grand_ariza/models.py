from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from user.models import User
from user.choices import BolimChoice



class Ariza(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    oquv = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(100))], default=0)
    manaviyat = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(100))], default=0)
    ilmiy = models.IntegerField(validators=[MinValueValidator(0, MaxValueValidator(100))], default=0)
    ariza_role = models.CharField(max_length=30, choices=BolimChoice.choices, default=BolimChoice.OQUV)
    tasdiqlash = models.BooleanField(default=False)
    rad_etish = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    


class Natija(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

