from django.db import models

# Create your models here.
class Readings(models.Model):
    sensor = models.IntegerField(default=0)
    datetime = models.CharField(max_length=200)
    id = models.IntegerField(primary_key=True)
    temp = models.FloatField()
    humidity = models.FloatField()
    pm25 = models.FloatField()
    pm10 = models.FloatField()

    def __str__(self):
        ret = "Sensor: " + str(self.sensor) + "Temp: " + str(self.temp)
        return ret