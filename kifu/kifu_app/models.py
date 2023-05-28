from django.db import models

class kifu(models.Model):
  title = models.CharField(max_length=100)
  description = models.CharField(max_length=300)
  mail = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  donation_amount = models.IntegerField()
  
  def __str__(self):
    return self.title
