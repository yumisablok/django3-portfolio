from django.db import models

# Create your models here.

#yumi: data gets stored in db now.

class Blog(models.Model):
        # property of page
        title = models.CharField(max_length=200)
        description = models.TextField()
        date = models.DateField()
        # after this make migration in cmd

        def __str__(self):
            return self.title    
