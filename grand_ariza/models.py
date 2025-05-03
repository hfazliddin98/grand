from django.db import models
from user.models import User



class Ariza(models.Model):
    talaba = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    
