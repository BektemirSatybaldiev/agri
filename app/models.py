from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone


class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'seasons'


class Culture(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cultures'


class Farmer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'farmers'


class Plot(models.Model):
    contour = models.PolygonField(srid=4326)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE, default=None)
    season = models.ManyToManyField(Season)

    def __str__(self):
        return f"Это поле принадлежит {self.farmer.name} и посеяно {self.culture}"

    class Meta:
        verbose_name_plural = 'plots'


class Planting(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.culture.name} planted in {self.plot.farmer.name}'s plot in {', '.join([season.name for season in self.plot.season.all()])}"

    class Meta:
        verbose_name_plural = 'plantings'
