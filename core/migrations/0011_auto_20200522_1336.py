# Generated by Django 3.0.6 on 2020-05-22 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200522_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='core.School'),
        ),
    ]