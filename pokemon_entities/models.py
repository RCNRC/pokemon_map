from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название RUS")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название ENG")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название JAP")
    image = models.ImageField(blank=True, verbose_name="Изображение")
    description = models.CharField(max_length=1000, blank=True, verbose_name="Описание")
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Из кого эволюционирует',
        related_name='next_evolutions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    def __str__(self):
        return f"{self.title}"

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True, name="Pokemon", verbose_name="Покемон")
    pokemon_latitude = models.FloatField(name="Lat", verbose_name="Широта")
    pokemon_longitude = models.FloatField(name="Lon", verbose_name="Долгота")
    appeared_at = models.DateTimeField(name="Appeared", null=True, verbose_name="Появился в")
    disappeared_at = models.DateTimeField(name="Desappeared", null=True, verbose_name="Исчез в")
    pokemon_level = models.IntegerField(name="Level", null=True, verbose_name="Уровень")
    pokemon_health = models.IntegerField(name="Health", null=True, verbose_name="Здоровье")
    pokemon_strength = models.IntegerField(name="Strength", null=True, verbose_name="Сила")
    pokemon_defence = models.IntegerField(name="Defence", null=True, verbose_name="Защита")
    pokemon_stamina = models.IntegerField(name="Stamina", null=True, verbose_name="Выносливость")
    def __str__(self):
        return f"{self.Pokemon.title}"
