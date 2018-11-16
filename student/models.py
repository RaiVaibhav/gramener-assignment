from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField(default=18,validators=[
            MinValueValidator(5)
        ])
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name

    
