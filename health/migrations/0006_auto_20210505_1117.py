# Generated by Django 3.0.5 on 2021-05-05 16:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20210505_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivedimage',
            name='datetime',
        ),
        migrations.AddField(
            model_name='archivedimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='archivedimage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
