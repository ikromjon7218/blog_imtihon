# Generated by Django 4.2 on 2023-05-14 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_profil_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='level_amount',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='profil',
            name='level',
            field=models.FloatField(default=0.0),
        ),
    ]
