# Generated by Django 2.2.8 on 2020-01-08 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0011_auto_20200108_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalproject',
            name='is_academic',
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_academic',
        ),
    ]
