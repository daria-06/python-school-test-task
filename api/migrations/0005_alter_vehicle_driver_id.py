# Generated by Django 3.2.9 on 2021-12-08 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_vehicle_driver_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='driver_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='api.driver'),
        ),
    ]
