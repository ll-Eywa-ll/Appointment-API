# Generated by Django 3.1.1 on 2020-09-25 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0034_appointmentdetail_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointmentdetail',
            name='category',
        ),
    ]