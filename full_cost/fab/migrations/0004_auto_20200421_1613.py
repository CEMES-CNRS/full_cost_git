# Generated by Django 2.2.8 on 2020-04-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fab', '0003_auto_20200214_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment',
            name='exp_type',
            field=models.CharField(choices=[('CLEANR', 'Clean Room Processes'), ('GROWTH', 'Growth')], default='CLEANR', max_length=200),
        ),
    ]
