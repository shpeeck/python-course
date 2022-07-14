from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255, verbose_name='name')
    description = models.CharField(max_length=800, verbose_name='description')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='rating')
    owner = models.ForeignKey('auth.User', related_name='owner', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(
        choices=(
            ('active', 'Active'), 
            ('deactivated', 'Deactivated'), 
            ('in_review', 'In_review')
        ), 
        max_length=20, 
        default='in_review')

    def __str__(self):
        return f"{self.name} {self.description} {self.rating}"

    # class Meta():
        # ordering = ['name']
