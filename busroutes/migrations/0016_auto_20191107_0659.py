# Generated by Django 2.2.7 on 2019-11-07 01:29

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('busroutes', '0015_auto_20191002_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='aliases',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='aliases'),
        ),
        migrations.AlterField(
            model_name='route',
            name='direction',
            field=models.CharField(choices=[('U', 'Up'), ('D', 'Down')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.IntegerField(choices=[(1, 'DTC'), (2, 'Delhi Transit')], default=1),
        ),
        migrations.AlterField(
            model_name='route',
            name='uid',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='stage',
            name='aliases',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='aliases'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='uid',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]
