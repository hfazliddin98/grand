import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.choices import UserRoleChoice



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    role = models.CharField(max_length=30, choices=UserRoleChoice.choices, default=UserRoleChoice.TALABA)
    fakultet = models.CharField(max_length=255, blank=True)
    yonalish = models.CharField(max_length=255, blank=True)
    kurs  = models.CharField(max_length=255, blank=True)
    guruh = models.CharField(max_length=255, blank=True)
    gpa = models.CharField(max_length=255, blank=True)
    parol = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-date_joined']


class AsosiyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        abstract = True



