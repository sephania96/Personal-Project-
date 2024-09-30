from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    movie_type = models.CharField(max_length=200,default='Action')
    image = models.ImageField(upload_to='project_image/', blank=True)