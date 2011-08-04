from GLIDEAPP.models import event,country,GLIDE
from django.contrib import admin
from django.contrib.gis import admin
#sort out tht inlines later
class eventAdmin(admin.ModelAdmin):
    pass

admin.site.register(event,eventAdmin)
admin.site.register(country)
admin.site.register(GLIDE,admin.GeoModelAdmin)
