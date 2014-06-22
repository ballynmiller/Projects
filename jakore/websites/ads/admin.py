from django.contrib import admin 
from websites.ads.models import Ad

class AdAdmin(admin.ModelAdmin):
    list_display=('name','location',)
admin.site.register(Ad,AdAdmin)