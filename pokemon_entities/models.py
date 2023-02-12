from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True)
    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, name="Pokemon")
    pokemon_latitude = models.FloatField(name="Lat")
    pokemon_longitude = models.FloatField(name="Lon")
    appeared_at = models.DateTimeField(name="Appeared at", null=True)
    disappeared_at = models.DateTimeField(name="Desappeared at", null=True)
