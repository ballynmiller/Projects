from websites.content.models import Banner, Section
from websites.shopping.models import Item
from django.contrib import admin 

class SectionAdmin(admin.ModelAdmin):
    list_display=('name','parent',)

admin.site.register(Banner)
admin.site.register(Section,SectionAdmin)