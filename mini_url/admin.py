from django.contrib import admin

# Register your models here.
from mini_url.models import MiniURL


class MiniURLAdmin(admin.ModelAdmin):
    list_display = ('url', 'code', 'date', 'pseudo', 'nombre_acces')
    list_filter = ('pseudo',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('url',)


admin.site.register(MiniURL, MiniURLAdmin)
