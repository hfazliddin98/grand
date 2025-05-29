from django.urls import path
from rest_framework.routers import SimpleRouter
from user.views import UserViewSet
from user.views import home, kirish, chiqish, admin_qoshish, adminlar



router = SimpleRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    path('', home, name='home'),
    path('kirish/', kirish, name='kirish'),
    path('admin_qoshish/', admin_qoshish, name='admin_qoshish'),
    path('chiqish/', chiqish, name='chiqish'),
    
    path('adminlar/', adminlar, name='adminlar'),
]

urlpatterns += router.urls
