import json
from django.core.management.base import BaseCommand

from tests.factories import CategoryFactory, CityFactory, AdvertFactory


class Command(BaseCommand):
    help = 'Generate fixture data for categories, cities, and adverts.'

    def handle(self, *args, **kwargs):
        AdvertFactory.create_batch(900)
