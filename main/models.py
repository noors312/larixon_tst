from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Name of the category",
        unique=True, db_index=True
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Name of the city",
        unique=True, db_index=True
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Advert(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    description = models.TextField()
    city = models.ForeignKey(
        City, on_delete=models.SET_NULL, null=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.title

    def increment_views_count(self):
        self.views += 1
        self.save(update_fields=['views'])
