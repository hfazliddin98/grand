from django.urls import path
from user.views import home, kirish, chiqish, royhat, adminlar

urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('royhat/', royhat, name='royhat'),
    path('chiqish/', chiqish, name='chiqish'),
    
    path('adminlar/', adminlar, name='adminlar'),
]
