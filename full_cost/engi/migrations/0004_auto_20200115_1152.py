# Generated by Django 2.2.8 on 2020-01-15 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0015_extraction_submitted'),
        ('engi', '0003_auto_20191220_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='workon',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.Group'),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='experiment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lab.User', verbose_name='Worker'),
        ),
    ]
