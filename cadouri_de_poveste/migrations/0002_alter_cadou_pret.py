# Generated by Django 4.1.3 on 2022-12-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadouri_de_poveste', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadou',
            name='pret',
            field=models.CharField(max_length=200),
        ),
    ]
