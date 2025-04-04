from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='plant_thumbnails/')
    image_folder = models.CharField(max_length=255)  # folder name under /media/plant_360/

    def __str__(self):
        return self.name
