# Generated by Django 5.1.2 on 2024-11-20 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_event_max_attendee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='max_attendee',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
