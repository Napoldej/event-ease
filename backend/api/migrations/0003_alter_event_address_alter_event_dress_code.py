# Generated by Django 5.1.2 on 2024-10-31 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_attendeeuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='dress_code',
            field=models.CharField(choices=[('CASUAL', 'Casual'), ('SMART_CASUAL', 'Smart Casual'), ('BUSINESS_CASUAL', 'Business Casual'), ('SEMI_FORMAL', 'Semi-Formal'), ('FORMAL', 'Formal'), ('BLACK_TIE', 'Black Tie'), ('WHITE_TIE', 'White Tie'), ('THEMED', 'Themed Dress Code'), ('OUTDOOR_BEACH_CASUAL', 'Outdoor/Beach Casual')], default='CASUAL', max_length=20),
        ),
    ]
