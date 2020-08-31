from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    imagePath = models.CharField(max_length=255)
    imageAlt = models.CharField(max_length=127)
    fullImagePath = models.CharField(max_length=255)
    siteURL = models.CharField(max_length=255)
    gitURL = models.CharField(max_length=255)

    def __str__(self):
        return self.title