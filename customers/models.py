from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    pass


class Customer(models.Model):

    MENU_CHOICES = ( 
        ('Breakfast','Breakfast'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )

    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    phone_number = models.IntegerField(default = 0)
    billed = models.BooleanField(default = False)
    meal = models.CharField(choices = MENU_CHOICES, max_length = 100)
    special_files = models.FileField(blank = True, null = True)
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email
