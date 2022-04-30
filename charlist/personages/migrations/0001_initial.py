# Generated by Django 3.2 on 2022-04-28 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('pronoun', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]