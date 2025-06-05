from django.urls import path
from grand_ariza.views import arizalar, natijalar, talaba_ariza_create

urlpatterns = [
    path('arizalar/', arizalar, name='arizalar'),
    path('natijalar/', natijalar, name='natijalar'),
    path('talaba_ariza_create/', talaba_ariza_create, name='talaba_ariza_create'),
]
