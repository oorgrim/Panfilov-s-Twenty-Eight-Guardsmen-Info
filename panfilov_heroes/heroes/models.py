from django.db import models

class Hero(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='hero_photos/', null=True, blank=True)
    
    birth_date = models.CharField(max_length=400)
    birth_place = models.CharField(max_length=400, null=True, blank=True)
    death_date = models.CharField(max_length=100)
    death_place = models.CharField(max_length=400, null=True, blank=True)
    connection_to_division = models.TextField(null=True, blank=True) 
    rank = models.CharField(max_length=400, null=True, blank=True)
    death_circumstances = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
