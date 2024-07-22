# Generated by Django 5.0.6 on 2024-07-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('bicyclettes', '0001_initial'), ('bicyclettes', '0002_alter_bicyclette_identifiant_unique_and_more'), ('bicyclettes', '0003_alter_bicyclette_systeme_de_freinage')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicyclette',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marque_et_modele', models.CharField(max_length=40, verbose_name='marque et modèle')),
                ('identifiant_unique', models.CharField(max_length=20, unique=True, verbose_name='identifiant unique')),
                ('a_une_assistance_electrique', models.BooleanField(default=False, verbose_name='a une une assistance électrique ?')),
                ('systeme_de_freinage', models.CharField(choices=[('VBR', 'v-brake (patins sur roue)'), ('DME', 'à disques mécanique'), ('DHY', 'à disques hydraulique'), ('PHY', 'à patins hydraulique')], max_length=3, verbose_name='systeme de freinage')),
            ],
            options={
                'verbose_name': 'bicyclettes',
                'verbose_name_plural': 'bicyclettes',
            },
        ),
    ]
