from django.db import models


class Personage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    pronoun = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    # user_id = models.IntegerField(на табл пользователей)
    # group_id = models.ForeignKey(на группу пользователей)

    def __str__(self):
        return f"Personage: \n" \
               f"name: {self.name!r}, pronoun: {self.pronoun!r}, " \
               f"description: {self.description!r}, parties: {self.get_parties()}"

    def get_parties(self):
        party = self.personageparty_set.all()
        return ', '.join(map(str, party))


class PersonageAspectsSet(models.Model):  # через ForeignKey - по идее - 1 ко многим
    id = models.IntegerField(primary_key=True)
    value1 = models.CharField(max_length=256)
    value2 = models.CharField(max_length=256)
    value3 = models.CharField(max_length=256)
    value4 = models.CharField(max_length=256)
    value5 = models.CharField(max_length=256, blank=True)
    personage = models.ForeignKey(Personage, on_delete=models.CASCADE)  # пишем модель и поле on_delete

    def __str__(self):
        return f"Personage: {self.personage.name},\n" \
               f"Aspects:\n" \
               f"{self.value1!r}\n" \
               f"{self.value2!r}\n" \
               f"{self.value3!r}\n" \
               f"{self.value4!r}\n" \
               f"{self.value5!r}"


class PersonageStunts(models.Model):  # через OneToOneField - по идее - 1 к 1
    personage = models.OneToOneField('personages.Personage',  # сработает и просто название класса Personage
                                     primary_key=True,
                                     on_delete=models.CASCADE)  # пишем модель и поле on_delete
    stunts = models.TextField(blank=True)

    def __str__(self):
        return f"Personage: {self.personage.name}, stunt: {self.stunts}"


class PersonageParty(models.Model):
    party = models.CharField(max_length=64)
    personage = models.ManyToManyField(Personage)

    def __str__(self):
        return self.party
