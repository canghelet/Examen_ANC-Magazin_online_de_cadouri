# Generated by Django 4.1.3 on 2022-12-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadouri_de_poveste', '0004_alter_cadou_pret'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('pret_total', models.FloatField()),
                ('numar_cadouri', models.PositiveIntegerField()),
                ('cos_inchis', models.BooleanField(default=False)),
                ('cadouri', models.ManyToManyField(to='cadouri_de_poveste.cadou')),
            ],
        ),
    ]
