from django.contrib import admin

from pers_stats.models import Skills
from personages.models import Personage, PersonageAspectsSet, PersonageStunts, PersonageParty


admin.site.register(Skills)
admin.site.register(Personage)
admin.site.register(PersonageAspectsSet)
admin.site.register(PersonageStunts)
admin.site.register(PersonageParty)
