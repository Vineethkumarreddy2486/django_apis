from django.db import models
from django.core.validators import MinValueValidator
from .validators import only_positive

# Create your models here.
class Product(models.Model):
    p_name = models.CharField(max_length=30)
    p_price= models.DecimalField(max_digits=10,decimal_places=2,validators=[only_positive])
    p_details=models.CharField(max_length=100)
    p_quantity=models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.p_name