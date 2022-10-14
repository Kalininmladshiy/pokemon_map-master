from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(verbose_name='имя покемона', max_length=200)
    title_en = models.CharField(
        verbose_name='имя покемона на английском',
        max_length=200,
        blank=True,
     )
    title_jp = models.CharField(
        verbose_name='имя покемона на японском',
        max_length=200,
        blank=True,
     )
    photo = models.ImageField(verbose_name='изображение покемона', null=True)
    description = models.TextField(
        verbose_name='описание покемона',
        blank=True,
     )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name='из кого эволюционирует',
        related_name='children',
        null=True,
        blank=True,
     )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='широта', null=True, blank=True)
    lon = models.FloatField(verbose_name='долгота', null=True, blank=True)
    pokemon = models.ForeignKey(
        Pokemon,
        verbose_name='покемон',
        related_name='entity',
        on_delete=models.CASCADE,
     )
    appeared_at = models.DateTimeField(
        verbose_name='когда появился',
        null=True,
        blank=True,
     )
    disappeared_at = models.DateTimeField(
        verbose_name='когда пропал',
        null=True,
        blank=True,
     )
    level = models.IntegerField(verbose_name='уровень', default=1)
    health = models.IntegerField(verbose_name='здоровье', default=1)
    strength = models.IntegerField(verbose_name='сила', default=1)
    defence = models.IntegerField(verbose_name='защита', default=1)
    stamina = models.IntegerField(verbose_name='выносливость', default=1)
