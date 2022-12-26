from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField(max_length=30)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    is_special = models.BooleanField(default=False)
    is_vegan = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    category = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, related_name='foods')
    topping = models.ManyToManyField(Topping, related_name='foods')

    def __str__(self):
        return self.name
