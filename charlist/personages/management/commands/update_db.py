from django.core.management.base import BaseCommand

from personages.models import Personage, PersonageStunts, PersonageAspectsSet


class Command(BaseCommand):

    def handle(self, *args, **options):
        # to_find_stunt = PersonageStunts.objects.filter(personage_id__id=1)
        # print(to_find_stunt)

        # find_stunt_by_name = PersonageStunts.objects.filter(stunts='st2').first()
        # filter отдает QuerySet (коллекция, а из нее N элемент), ленив - идет в БД только по запросу отфильтрованного
        # можно like(), last()

        # get() оборачивают в try-except
        # get должен отдавать уникальный объект. если 0 или >1 - ошибки
        # try:
        #     find_stunt_by_name = PersonageStunts.objects.get(stunts='st1')
        # except Exception as e:
        #     print(f"Cannot find {e}")
        # print(find_stunt_by_name, type(find_stunt_by_name))

        # можно фильтровать через __in, __like
        # to_find_stunt = PersonageAspectsSet.objects.filter(personage__description__in=('desc1', 'Second'))
        # print(to_find_stunt.query) # так можно увидеть сам SQL запрос

        # to_find_stunt = PersonageAspectsSet.objects.filter(value2=12)
        # to_find_stunt = PersonageAspectsSet.objects.filter(value2__gt=11) # gt - больше
        # to_find_stunt = PersonageAspectsSet.objects.filter(value2__gte=12) # gte - >=
        # print(to_find_stunt)

        to_find_empty_aspects = PersonageAspectsSet.objects.filter(value5='')
        # print(to_find_empty_aspects.query)
        print(to_find_empty_aspects)
        for aspect in to_find_empty_aspects:
            PersonageAspectsSet.objects.filter(value5='').update(
                value5='to be filled2'
            )
            print(f'for {aspect} detail created')
        print("Updating done")

        ## разобрать, почему без filter(value5='').update() обновляются все, а не только подошедшие под фильтр
