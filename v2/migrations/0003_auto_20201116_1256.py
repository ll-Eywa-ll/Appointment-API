# Generated by Django 3.1.1 on 2020-11-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v2', '0002_auto_20201115_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zorg',
            name='profile_photo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='zorg/profile_photo/'),
        ),
    ]
