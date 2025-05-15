from django.db import models
from django.contrib.auth.models import User



class Books(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField()
  cover = models.CharField(max_length=255,default="1")
  new_arrival = models.BooleanField(default=True)
  featured = models.BooleanField(default=False)
  
  
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('user', 'book')

class Review(models.Model):
    book = models.ForeignKey(Books, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)

