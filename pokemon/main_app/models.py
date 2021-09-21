from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.
MOVEATTRIBUTE = (
    ('Phys', 'Physical'),
    ('Spec', 'Special'),
    ('Stat', 'Status')
)


class Ribbon(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_name_display()} on {self.name}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    level = models.IntegerField()
    ribbons = models.ManyToManyField(Ribbon)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

class Move(models.Model):
        name = models.CharField(max_length=100)
        type = models.CharField(max_length=100)
        power = models.IntegerField()
        attribute = models.CharField(
            max_length=4,
            default=MOVEATTRIBUTE[0][0]
               
        )
        pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

        def __str__(self):
            return f"{self.get_attribute_display()} on {self.name}"



