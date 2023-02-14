from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название RUS")
    title_en = models.CharField(max_length=200, blank=True, verbose_name="Название ENG")
    title_jp = models.CharField(max_length=200, blank=True, verbose_name="Название JAP")
    image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    previous_evolution = models.ForeignKey(
        "self",
        verbose_name='Из кого эволюционирует',
        related_name='next_evolutions',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    def __str__(self):
        return self.title

class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, related_name="entity", on_delete=models.CASCADE, verbose_name="Покемон")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Появился в")
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name="Исчез в")
    level = models.IntegerField(null=True, blank=True, verbose_name="Уровень")
    health = models.IntegerField(null=True, blank=True, verbose_name="Здоровье")
    strength = models.IntegerField(null=True, blank=True, verbose_name="Сила")
    defence = models.IntegerField(null=True, blank=True, verbose_name="Защита")
    stamina = models.IntegerField(null=True, blank=True, verbose_name="Выносливость")
    def __str__(self):
        return self.pokemon.title
