from django.db import models

# Create your models here.
class event(models.Model):
	event = models.CharField("Event",max_length=120)
class country(models.Model):
	country = models.CharField("Event",max_length=120)
class GLIDE(models.Model):
	glidenumber = models.CharField("Glide Number",max_length=120)
	event = models.ForeignKey(event,null=False)
        country = models.ForeignKey(country,null=False)
        comment = models.TextField("Comment",null=False)
        
