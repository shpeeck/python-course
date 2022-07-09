from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.CharField(max_length=800, verbose_name='description')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='rating')

    def __str__(self):
        return f"{self.name} {self.rating}"

    class Meta():
        verbose_name =  'Store'
        verbose_name_plural = 'Stores'
