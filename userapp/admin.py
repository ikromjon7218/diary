from django.contrib import admin
from .models import *

# admin.site.register()

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_activity")
    list_display_links = ('id', 'name')
    # list_editable = ('name',)
    # list_filter = ('date_of_birth', "")
    list_per_page = 100
    search_fields = 'id', 'name', 'phone_number', 'email', 'date_of_birth', 'last_activity'
