from django.contrib import admin
from .models import Topping, FoodCategory, Food

admin.register(Topping, FoodCategory, Food)(admin.ModelAdmin)
