# Generated by Django 5.2.3 on 2025-07-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0005_alter_location_options_alter_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(choices=[('HEAVY', 'HEAVY'), ('LIGHT', 'LIGHT'), ('APV', 'APV')], max_length=50),
        ),
    ]
