from django.contrib import admin
from .models import *

# admin.site.register()

@admin.register(Error)
class ErrorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", )
    list_display_links = ('id',)
    # list_editable = ('name',)
    # list_filter = ('unit', "book")
    list_per_page = 100
    search_fields = 'id', 'name', "description"

@admin.register(Daily)
class DailyAdmin(admin.ModelAdmin):
    list_display = ("id", "pray", "bed_time", "date")
    list_display_links = ('id', "pray")
    # list_editable = ('name',)
    # list_filter = ('unit', "book")
    list_per_page = 100
    search_fields = 'id', 'bed_time', "date", "event"

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "date_added")
    list_display_links = ('id', "name",)
    # list_editable = ('name',)
    # list_filter = ('unit', "book")
    list_per_page = 100
    search_fields = 'id', 'name', "description", "date_added"
