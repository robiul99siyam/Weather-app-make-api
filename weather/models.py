from django.db import models

# Create your models here.

DESCRIPTION = (
    (0,"Sunny"),
    (1,"Rain"),
    (2,"Cloudy"),
    (3,"Snow")

)

class  Description(models.Model):
    """ Weather model create here """

    weather_dercription = models.IntegerField(choices=DESCRIPTION,default=0)
    temparature = models.FloatField()
    create_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_on']
    

    def __str__(self):
        return str(self.create_on)
