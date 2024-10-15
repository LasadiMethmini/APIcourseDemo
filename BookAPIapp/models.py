from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=225)
    author=models.CharField(max_length=225)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    class Meta:
        models.Index(fields=['price']),