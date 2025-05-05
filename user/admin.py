from django.contrib import admin
from user.models import User



@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['username', 'parol', 'password']
    fields = ['username', 'last_name', 'first_name', 'role']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'superadmin':
            return qs
        elif request.user.role == 'admin':
            return qs.filter(role='talaba')
        return qs.none()
