from django.db import models

class Books(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  
  #def __str__(self):
    #return 