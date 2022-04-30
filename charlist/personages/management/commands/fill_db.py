# здесь можно создать конкретные данные для БД

from django.core.management.base import BaseCommand

from personages.models import PersonageParty


class Command(BaseCommand):

    def handle(self, *args, **options):
        parties = ['forest', 'Sands', 'Dungeon']
        for party in parties:
            PersonageParty.objects.get_or_create(party=party)  # 1 - поле в Бд, 2 - значение
