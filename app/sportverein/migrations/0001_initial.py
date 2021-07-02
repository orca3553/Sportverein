# Generated by Django 3.2.4 on 2021-06-30 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beitraege',
            fields=[
                ('betragid', models.AutoField(db_column='betragID', primary_key=True, serialize=False)),
                ('bisalter', models.IntegerField(db_column='bisAlter')),
                ('betrag', models.IntegerField(db_column='Betrag')),
                ('gueltig_ab', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leistungsniveaus',
            fields=[
                ('niveauid', models.AutoField(db_column='niveauID', primary_key=True, serialize=False)),
                ('beschreibung', models.CharField(blank=True, max_length=255, null=True)),
                ('niveauname', models.CharField(db_column='niveauName', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mitglieder',
            fields=[
                ('mitgliedid', models.AutoField(db_column='mitgliedID', primary_key=True, serialize=False)),
                ('iban', models.CharField(db_column='IBAN', max_length=255)),
                ('vname', models.CharField(db_column='vName', max_length=255)),
                ('nname', models.CharField(db_column='nName', max_length=255)),
                ('tel', models.CharField(db_column='Tel', max_length=255)),
                ('gebdat', models.DateField(db_column='GebDat')),
            ],
        ),
        migrations.CreateModel(
            name='Orte',
            fields=[
                ('ortid', models.AutoField(db_column='ortID', primary_key=True, serialize=False)),
                ('bezeichnung', models.CharField(max_length=255)),
                ('art', models.CharField(max_length=255)),
                ('strasse', models.CharField(blank=True, max_length=255, null=True)),
                ('kontakt', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sportarten',
            fields=[
                ('sportartid', models.AutoField(db_column='sportartID', primary_key=True, serialize=False)),
                ('bezeichnung', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainerid', models.AutoField(db_column='trainerID', primary_key=True, serialize=False)),
                ('nname', models.CharField(db_column='nName', max_length=255)),
                ('vname', models.CharField(blank=True, db_column='vNAme', max_length=255, null=True)),
                ('tel', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Zahlungen',
            fields=[
                ('zahlungid', models.AutoField(db_column='zahlungID', primary_key=True, serialize=False)),
                ('datum', models.DateField()),
                ('betrag', models.IntegerField()),
                ('mitgliedid', models.ForeignKey(blank=True, db_column='mitgliedID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.mitglieder')),
            ],
        ),
        migrations.CreateModel(
            name='Uebungsgruppen',
            fields=[
                ('uebungsgruppenid', models.AutoField(db_column='uebungsgruppenID', primary_key=True, serialize=False)),
                ('uebungsgruppenname', models.CharField(blank=True, db_column='uebungsgruppenName', max_length=255, null=True)),
                ('maxteilnehmer', models.IntegerField(db_column='maxTeilnehmer')),
                ('wochentag', models.CharField(blank=True, max_length=255, null=True)),
                ('startzeit', models.DateField(blank=True, null=True)),
                ('niveauid', models.ForeignKey(blank=True, db_column='niveauID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.leistungsniveaus')),
                ('ortid', models.ForeignKey(blank=True, db_column='ortID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.orte')),
                ('sportartid', models.ForeignKey(blank=True, db_column='sportartID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.sportarten')),
                ('trainerid', models.ForeignKey(blank=True, db_column='trainerID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Trainingseinheit',
            fields=[
                ('trainingseinheitid', models.AutoField(db_column='trainingseinheitID', primary_key=True, serialize=False)),
                ('datum', models.DateField()),
                ('anmerkung', models.CharField(blank=True, max_length=255, null=True)),
                ('uebungsgruppenid', models.ForeignKey(blank=True, db_column='uebungsgruppenID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.uebungsgruppen')),
            ],
        ),
        migrations.CreateModel(
            name='Ruhend',
            fields=[
                ('ruhendid', models.AutoField(db_column='ruhendID', primary_key=True, serialize=False)),
                ('startdat', models.DateField(db_column='startDat')),
                ('enddat', models.DateField(blank=True, db_column='endDat', null=True)),
                ('anmerk', models.CharField(blank=True, max_length=255, null=True)),
                ('mitgliedid', models.ForeignKey(blank=True, db_column='mitgliedID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.mitglieder')),
            ],
        ),
        migrations.CreateModel(
            name='Anmeldungen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anmeldungdatum', models.DateField(blank=True, null=True)),
                ('mitgliedid', models.ForeignKey(blank=True, db_column='mitgliedID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.mitglieder')),
                ('uebungsgruppenid', models.ForeignKey(blank=True, db_column='uebungsgruppenID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sportverein.uebungsgruppen')),
            ],
        ),
    ]
