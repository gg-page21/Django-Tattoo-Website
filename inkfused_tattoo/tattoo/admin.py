from django.contrib import admin
from .models import Tattoo

# Register your models here.

class TattooAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    
admin.site.register(Tattoo, TattooAdmin)
