from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pseudonym = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.pseudonym

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title