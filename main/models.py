from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=60),
    city = models.CharField(max_length=30),
    place = models.CharField(max_length=50),
    description = models.TextField(),
    event_date = models.DateField(null=True, blank=True),
    event_hour = models.DateTimeField()
    photo = models.ImageField(null=True, blank=True)

    def _str_(self):
        return self.name

    def event_des(self):
        return str(self.name) + " (" + str(self.place) + " " + str(self.city) + " )"
