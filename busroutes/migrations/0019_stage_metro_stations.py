# Generated by Django 2.2.7 on 2020-03-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busroutes', '0018_metrostation'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='metro_stations',
            field=models.ManyToManyField(to='busroutes.MetroStation'),
        ),
    ]
