# Generated by Django 3.0.5 on 2021-06-07 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0013_auto_20210607_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
