# Generated by Django 3.2 on 2022-04-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personages', '0004_rename_user_id_personageaspectsset_personage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personageaspectsset',
            name='value5',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
