# Generated by Django 4.0.5 on 2022-06-20 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akeray', '0004_alter_renter_options_renter_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
