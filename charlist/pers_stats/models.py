from django.db import models


class Skills(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    # __table_args__ = (
    #     CheckConstraint('value <= 5'),
    # ) какое-то надо ограничение

    def __str__(self):
        return f"{self.name!r}"
