# Generated by Django 3.2.7 on 2021-09-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_ribbon_pokemon_ribbons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='attribute',
            field=models.CharField(default='Phys', max_length=4),
        ),
    ]