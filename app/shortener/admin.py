from django.contrib import admin
from app.shortener.models import Shortener

# Register your models here.
class ShortenerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    search_fields = (
        'url',
        'alias',
    )
    list_display = (
        'id',
        'get_url',
        'alias',
        'get_snippet',
        'count',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'count',
    )

admin.site.register(Shortener, ShortenerAdmin)
