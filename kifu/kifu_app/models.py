from django.db import models

class user(models.Model):
  mail = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  total_donation_amounts = models.IntegerField()
  
  def __str__(self):
    return self.mail

class donation(models.Model):
  donation_amount = models.IntegerField()
  user = models.ForeignKey(user, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.id