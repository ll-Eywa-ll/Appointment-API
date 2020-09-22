# Generated by Django 3.0.9 on 2020-09-22 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200921_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='api.Categories'),
        ),
        migrations.AlterField(
            model_name='service',
            name='zorg',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='zorg', to='api.Zorg'),
        ),
    ]