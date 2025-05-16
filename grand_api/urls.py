from django.urls import path
from rest_framework.routers import SimpleRouter
from grand_api.views import ArizaViewSet


router = SimpleRouter()
router.register(r'arizalar', ArizaViewSet)



urlpatterns = []

urlpatterns += router.urls
