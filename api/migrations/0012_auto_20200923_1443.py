# Generated by Django 3.1.1 on 2020-09-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200923_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(max_length=5),
        ),
    ]