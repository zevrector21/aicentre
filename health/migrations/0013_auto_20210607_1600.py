# Generated by Django 3.0.5 on 2021-06-07 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_auto_20210607_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
