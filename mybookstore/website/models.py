from django.db import models

# Create your models here.
class Books(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
