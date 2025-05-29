from django.contrib import admin
from grand_ariza.models import Ariza, Natija

@admin.register(Ariza)
class ArizaAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Natija)
class NatijaAdmin(admin.ModelAdmin):
    list_display = ['id']

