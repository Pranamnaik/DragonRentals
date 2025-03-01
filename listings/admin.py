from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'property_type', 'location', 'rent', 'landlord')
    list_filter = ('property_type', 'location')
    search_fields = ('title', 'description', 'location')
    readonly_fields = ('created_at', 'updated_at')
