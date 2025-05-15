from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('haker/', admin.site.urls),
    path('', include("user.urls")),
    path('grand_ariza/', include("grand_ariza.urls")),
]
