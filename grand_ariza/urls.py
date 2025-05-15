from django.urls import path
from grand_ariza.views import arizalar, natijalar

urlpatterns = [
    path('arizalar/', arizalar, name='arizalar'),
    path('natijalar/', natijalar, name='natijalar'),
]
