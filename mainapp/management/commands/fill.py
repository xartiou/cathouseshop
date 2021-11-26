import json

from django.core.management.base import BaseCommand


def load_from_json(path):
    with open(path, 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
