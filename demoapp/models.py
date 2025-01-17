from django.db import models

# Create your models here.


class Health(models.Model):
    name = models.CharField(max_length=250)
    images = models.ImageField(upload_to='pictures')
    desc = models.TextField()

    def __str__(self):
        return self.name

