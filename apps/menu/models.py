from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.URLField()
    category = models.ForeignKey( Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name