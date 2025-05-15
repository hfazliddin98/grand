from django.db import models

class ArizaRoleChoice(models.TextChoices):
    OQUV = ("oquv", "oquv")
    MANAVIYAT = ("manaviyat", "manaviyat")
    ILMIY = ("ilmiy", "ilmiy")