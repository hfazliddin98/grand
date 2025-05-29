from django.db import models

class UserRoleChoice(models.TextChoices):
    SUPERADMIN = ("superadmin", "superadmin")
    ADMIN = ("admin", "admin")
    TALABA = ("talaba", "talaba")

class BolimChoice(models.TextChoices):
    OQUV = ("oquv", "oquv")
    MANAVIYAT = ("manaviyat", "manaviyat")
    ILMIY = ("ilmiy", "ilmiy")