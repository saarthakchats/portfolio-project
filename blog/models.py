from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField()
    blogimg = models.ImageField(upload_to='images/')
