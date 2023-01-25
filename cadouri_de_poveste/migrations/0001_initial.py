# Generated by Django 4.1.3 on 2022-12-10 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadou',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=600)),
                ('pret', models.PositiveIntegerField()),
                ('cod', models.CharField(max_length=200)),
                ('categorie', models.CharField(choices=[('cadouri_femei', 'cadouri_femei'), ('cadouri_barbati', 'cadouri_barbati'), ('cadouri_copii', 'cadouri_copii'), ('ambalare_cadou', 'ambalare_cadou')], max_length=200)),
                ('descriere', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=200)),
                ('parola', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('adresa', models.CharField(max_length=600)),
                ('telefon', models.PositiveIntegerField()),
                ('logat', models.BooleanField(default=False)),
            ],
        ),
    ]