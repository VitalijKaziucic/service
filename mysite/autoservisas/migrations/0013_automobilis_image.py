# Generated by Django 4.1.1 on 2022-09-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservisas', '0012_alter_automobilis_vehicle_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='automobilis',
            name='image',
            field=models.ImageField(null=True, upload_to='covers'),
        ),
    ]
