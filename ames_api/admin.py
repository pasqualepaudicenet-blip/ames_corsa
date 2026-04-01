from django.contrib import admin
from .models import CustomUser, Corsa, Sample
from django.contrib.auth.admin import UserAdmin

admin.site.register(CustomUser, UserAdmin)

@admin.register(Corsa)
class CorsaAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'type', 'description') # Colonne visibili nella lista
    search_fields = ('description', 'type')             # Barra di ricerca
    list_filter = ('date', 'type')                      # Filtri laterali

@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('sampleId', 'sampleName', 'corsa')
    search_fields = ('sampleName',)
    list_filter = ('corsa',)
