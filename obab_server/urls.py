from django.contrib import admin
from django.urls import path, include
from obab_server.swagger import get_swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('recipes.urls')),
    path('accounts/',include('accounts.urls')),
]

urlpatterns += get_swagger_urls()
