# Generated by Django 3.0.3 on 2020-02-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reading',
            name='humidity',
            field=models.FloatField(),
        ),
    ]
