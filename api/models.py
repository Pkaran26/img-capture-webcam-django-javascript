from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=25)

    def __str__(self):
        return self.category

class Images(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.ImageField()

    def __str__(self):
        return self.category.category
