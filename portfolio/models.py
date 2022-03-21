from django.db import models

# Create your models here.
# yumi:
class Project(models.Model):
    # property of page
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
# whether there will be a url or not so we set blank property, by default it is false
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
