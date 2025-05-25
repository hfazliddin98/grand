from django.contrib import admin
from user.choices import BolimChoice
from grand_ariza.models import Ariza

@admin.register(Ariza)
class ArizaAdmin(admin.ModelAdmin):
    list_display = ['id']

    def get_fields(self, request, obj=None):
        if request.user.role == 'superadmin':
            return ['user']
        elif request.user.role == 'admin':
            if request.user.bolim == BolimChoice.OQUV:
                return ['oquv']  # 'role' ni ko'rsatmaydi
            elif request.user.bolim == BolimChoice.MANAVIYAT:
                return ['manaviyat']
            elif request.user.bolim == BolimChoice.ILMIY:
                return ['ilmiy']
        return []