from django.db import models

# Create your models here.
class PokemonData(models.Model):
    #date = models.DateTimeField()
    json_data = models.JSONField()

    # def __str__(self):
    #     return self.date


class Pokemon(models.Model):
    name = models.CharField(max_length=240, unique=True)
    url = models.CharField(max_length=240)
    image_url = models.CharField(max_length=240)

    def __str__(self):
        return self.name
