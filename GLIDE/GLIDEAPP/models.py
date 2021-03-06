from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class event(models.Model):
	event = models.CharField("Event",max_length=120)
        def __unicode__(self):
		return self.event
class country(models.Model):
	country = models.CharField("Event",max_length=120)
        def __unicode__(self):
		return self.country
        class Meta:
		verbose_name_plural = "Countries"
class GLIDE(models.Model):
	glidenumber = models.CharField("Glide Number",max_length=120)
	event = models.ForeignKey(event,null=False)
        country = models.ForeignKey(country,null=False)
        comment = models.TextField("Comment",null=False)
        #we now add the GIS juice over here
        polygeom = models.MultiPolygonField()
        objects = models.GeoManager()
        def __unicode__(self):
		return self.glidenumber
        class Meta:
		verbose_name_plural = "GLIDE Occurences"
        
