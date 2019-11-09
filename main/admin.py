from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    #fields = (' name', 'description')
    list_display = ('name', 'description')
    search_fields = ('name', 'description', 'place')




# Register your models here.
