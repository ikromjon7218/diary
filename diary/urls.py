from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin_panel/', admin.site.urls),
]
