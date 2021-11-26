import json
from django.conf import settings
from django.core.management.base import BaseCommand


def load_from_json(file_name):
    with open(f"{settings.BASE_dir}/json/{file_name}.json", 'r') as json_file:
        return json.load(json_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
