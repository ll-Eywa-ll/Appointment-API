# Generated by Django 3.0.9 on 2020-08-25 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_appointment_totaltime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Gender'),
        ),
    ]
