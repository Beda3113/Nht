import csv
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Импорт телефонов из CSV-файла'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Путь к CSV-файлу')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            # Преобразуем данные из CSV в формат, подходящий для модели Phone
            phone = Phone(
                id=phone_data['id'],
                name=phone_data['name'],
                price=float(phone_data['price']),  # Цена должна быть числом
                image=phone_data['image'],
                release_date=phone_data['release_date'],  # Дата выпуска
                lte_exists=(phone_data['lte_exists'].lower() == 'true')  # Преобразуем строку в boolean
            )
            phone.save()  # Сохраняем объект в базу данных

        self.stdout.write(self.style.SUCCESS('Телефоны успешно импортированы'))
