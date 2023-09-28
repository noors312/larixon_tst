import factory
from factory.django import DjangoModelFactory

from main.models import Category, Advert, City


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: f'Category {n}')


class CityFactory(DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Sequence(lambda n: f'City {n}')


class AdvertFactory(DjangoModelFactory):
    class Meta:
        model = Advert

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    city = factory.SubFactory(CityFactory)
    category = factory.SubFactory(CategoryFactory)
    views = 0  # Set the views to 0 by default
