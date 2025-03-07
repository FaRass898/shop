from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True),
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True),
    title = models.CharField(max_length=100),
    description = models.TextField(),
    price = models.DecimalField(max_digits=100, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    id = models.AutoField(primary_key=True),
    text = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
