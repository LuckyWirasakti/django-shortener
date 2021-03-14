from django.contrib import admin
from rangefilter.filter import DateRangeFilter
from app.shortener.models import Shortener, Statistic, Location, Source

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

class StatisticAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'get_shortener',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'shortener',
        ('created_at', DateRangeFilter),
    )

admin.site.register(Statistic, StatisticAdmin)

class LocationAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'locale',
        'get_shortener',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'locale',
        'shortener',
    )
    
admin.site.register(Location, LocationAdmin)

class SourceAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'id',
        'reference',
        'get_shortener',
        'created_at',
        'updated_at',
    )
    list_filter = (
        'reference',
        'shortener',
    )
    
admin.site.register(Source, SourceAdmin)
