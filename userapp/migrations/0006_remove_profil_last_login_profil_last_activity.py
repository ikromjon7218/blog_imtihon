# Generated by Django 4.2 on 2023-05-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_profil_last_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='last_login',
        ),
        migrations.AddField(
            model_name='profil',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]