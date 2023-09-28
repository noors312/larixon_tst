from django.contrib import admin

from main.models import Category, City, Advert


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass
