# Generated by Django 3.2 on 2022-04-28 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personages', '0002_personageaspectsset'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonageStunts',
            fields=[
                ('personage', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='personages.personage')),
                ('stunts', models.TextField(blank=True)),
            ],
        ),
    ]