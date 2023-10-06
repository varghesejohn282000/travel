from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

class People(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics1')
    des=models.TextField()

    def __str__(self):
        return self.name
# Create your models here.


