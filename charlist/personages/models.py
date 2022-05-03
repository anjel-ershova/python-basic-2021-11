from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from myauth.models import CharlistUser


class Personage(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(CharlistUser, on_delete=models.SET_NULL, null=True)
    # group_id = models.ForeignKey(на группу пользователей)
    pers_name = models.CharField(max_length=64)
    pers_pronoun = models.CharField(max_length=64)
    pers_description = models.TextField(blank=True)
    refresh = models.IntegerField(null=True)
    fate_points = models.IntegerField(null=True)
    aspect1 = models.CharField(max_length=256, blank=True)
    aspect2 = models.CharField(max_length=256, blank=True)
    aspect3 = models.CharField(max_length=256, blank=True)
    aspect4 = models.CharField(max_length=256, blank=True)
    aspect5 = models.CharField(max_length=256, blank=True)
    approach1_name = models.CharField(max_length=256, blank=True)
    approach1_value = models.IntegerField(null=True)
    approach2_name = models.CharField(max_length=256, blank=True)
    approach2_value = models.IntegerField(null=True)
    approach3_name = models.CharField(max_length=256, blank=True)
    approach3_value = models.IntegerField(null=True)
    approach4_name = models.CharField(max_length=256, blank=True)
    approach4_value = models.IntegerField(null=True)
    approach5_name = models.CharField(max_length=256, blank=True)
    approach5_value = models.IntegerField(null=True)
    approach6_name = models.CharField(max_length=256, blank=True)
    approach6_value = models.IntegerField(null=True)
    stunts = models.TextField(blank=True)
    extras = models.TextField(blank=True)
    stress = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)], default=0)
    consequences_mild = models.CharField(max_length=256, blank=True)
    consequences_moderate = models.CharField(max_length=256, blank=True)
    consequences_severe = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"Personage: \n" \
               f"name: {self.pers_name!r}, pronoun: {self.pers_pronoun!r}, " \
               f"description: {self.pers_description!r}, parties: {self.get_parties()}"

    def get_parties(self):
        party = self.personageparty_set.all()
        return ', '.join(map(str, party))


class PersonageParty(models.Model):
    party = models.CharField(max_length=64)
    personage = models.ManyToManyField(Personage)

    def __str__(self):
        return self.party
