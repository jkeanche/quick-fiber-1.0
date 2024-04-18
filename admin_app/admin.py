from django.contrib import admin

from admin_app.models import Station, Invoice,County, Location, Estate

admin.site.register(Station)
admin.site.register(Invoice)
admin.site.register(County)
admin.site.register(Location)
admin.site.register(Estate)