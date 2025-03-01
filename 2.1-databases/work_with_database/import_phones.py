import csv
from django.core.management.base import BaseCommand
from phones.models import Phone  # Импортируем модель Phone

class Command(BaseCommand):
    help = 'Импорт телефонов из CSV-файла'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='phones.csv')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=(row['lte_exists'].lower() == 'true')
                )
                phone.save()

        self.stdout.write(self.style.SUCCESS('Телефоны успешно импортированы'))