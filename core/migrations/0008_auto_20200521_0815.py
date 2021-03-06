# Generated by Django 3.0.6 on 2020-05-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200521_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='time_minutes',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
