from django.contrib import admin
from base_app.models import *

admin.site.register(ItemList)
admin.site.register(Items)
admin.site.register(AboutUs)
admin.site.register(FeedBack)
@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ['Name', 'booking_date', 'status' ]
    list_filter = ['status']

admin.site.site_header = "padmini Admin Panel"
admin.site.site_title = "padmini Admin"
admin.site.index_title = "Restaurant Dashboard"

# Register your models here.
