from django.contrib import admin 
from websites.shopping.models import Item,Group,Size,Media

class ItemAdmin(admin.ModelAdmin):
    filter_horizontal=('section',)
admin.site.register(Item, ItemAdmin)

class GroupAdmin(admin.ModelAdmin):
    filter_horizontal=('items',)
admin.site.register(Group,GroupAdmin)
    
admin.site.register(Size)
admin.site.register(Media)
