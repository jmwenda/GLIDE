from GLIDEAPP.models import event,country,GLIDE
from django.contrib import admin
from django.contrib.gis import admin
#sort out tht inlines later
admin.site.register(event)
admin.site.register(country)
admin.site.register(GLIDE,admin.GeoModelAdmin)
