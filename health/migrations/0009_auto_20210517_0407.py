# Generated by Django 3.0.5 on 2021-05-17 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_auto_20210506_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detection',
            old_name='status',
            new_name='enable_the_detection',
        ),
    ]
