from django.db import models
from user.models import User



class Ariza(models.Model):
    talaba = models.OneToOneField(User, on_delete=models.CASCADE  )
    


class Natija(models.Model):
    talaba = models.OneToOneField(User, on_delete=models.CASCADE  )
    

