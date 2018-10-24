from django.db import models

# Create your models here.

class SocialNetwork(models.Model):

    name = models.CharField(max_length=50)
    url_to_page = models.URLField()
    icon = models.ImageField(default='default.png')

    def __str__(self):
        return self.name