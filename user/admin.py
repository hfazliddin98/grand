from django.contrib import admin
from user.models import User



@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'first_name', 'is_active', 'is_superuser']
    # fields = ['username', 'last_name', 'first_name', 'role', 'bolim', 'is_active', 'is_superuser']


