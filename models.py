from django.db import models

class Kegiatan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title
