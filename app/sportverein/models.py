from django.db import models


class Anmeldungen(models.Model):
    mitgliedid = models.ForeignKey('Mitglieder', models.DO_NOTHING, db_column='mitgliedID', blank=True, null=True)  # Field name made lowercase.
    uebungsgruppenid = models.ForeignKey('Uebungsgruppen', models.DO_NOTHING, db_column='uebungsgruppenID', blank=True, null=True)  # Field name made lowercase.
    anmeldungdatum = models.DateField(blank=True, null=True)


class Beitraege(models.Model):
    betragid = models.AutoField(db_column='betragID', primary_key=True)  # Field name made lowercase.
    bisalter = models.IntegerField(db_column='bisAlter')  # Field name made lowercase.
    betrag = models.IntegerField(db_column='Betrag')  # Field name made lowercase.
    gueltig_ab = models.DateField()


class Leistungsniveaus(models.Model):
    niveauid = models.AutoField(db_column='niveauID', primary_key=True)  # Field name made lowercase.
    beschreibung = models.CharField(max_length=255, blank=True, null=True)
    niveauname = models.CharField(db_column='niveauName', max_length=255)  # Field name made lowercase.


class Mitglieder(models.Model):
    mitgliedid = models.AutoField(db_column='mitgliedID', primary_key=True)  # Field name made lowercase.
    iban = models.CharField(db_column='IBAN', max_length=255)  # Field name made lowercase.
    vname = models.CharField(db_column='vName', max_length=255)  # Field name made lowercase.
    nname = models.CharField(db_column='nName', max_length=255)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=255)  # Field name made lowercase.
    gebdat = models.DateField(db_column='GebDat')  # Field name made lowercase.


class Orte(models.Model):
    ortid = models.AutoField(db_column='ortID', primary_key=True)  # Field name made lowercase.
    bezeichnung = models.CharField(max_length=255)
    art = models.CharField(max_length=255)
    strasse = models.CharField(max_length=255, blank=True, null=True)
    kontakt = models.CharField(max_length=255, blank=True, null=True)


class Ruhend(models.Model):
    ruhendid = models.AutoField(db_column='ruhendID', primary_key=True)  # Field name made lowercase.
    startdat = models.DateField(db_column='startDat')  # Field name made lowercase.
    enddat = models.DateField(db_column='endDat', blank=True, null=True)  # Field name made lowercase.
    anmerk = models.CharField(max_length=255, blank=True, null=True)
    mitgliedid = models.ForeignKey(Mitglieder, models.DO_NOTHING, db_column='mitgliedID', blank=True, null=True)  # Field name made lowercase.


class Sportarten(models.Model):
    sportartid = models.AutoField(db_column='sportartID', primary_key=True)  # Field name made lowercase.
    bezeichnung = models.CharField(max_length=255)


class Trainer(models.Model):
    trainerid = models.AutoField(db_column='trainerID', primary_key=True)  # Field name made lowercase.
    nname = models.CharField(db_column='nName', max_length=255)  # Field name made lowercase.
    vname = models.CharField(db_column='vNAme', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(max_length=255)


class Trainingseinheit(models.Model):
    trainingseinheitid = models.AutoField(db_column='trainingseinheitID', primary_key=True)  # Field name made lowercase.
    datum = models.DateField()
    anmerkung = models.CharField(max_length=255, blank=True, null=True)
    uebungsgruppenid = models.ForeignKey('Uebungsgruppen', models.DO_NOTHING, db_column='uebungsgruppenID', blank=True, null=True)  # Field name made lowercase.


class Uebungsgruppen(models.Model):
    uebungsgruppenid = models.AutoField(db_column='uebungsgruppenID', primary_key=True)  # Field name made lowercase.
    uebungsgruppenname = models.CharField(db_column='uebungsgruppenName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maxteilnehmer = models.IntegerField(db_column='maxTeilnehmer')  # Field name made lowercase.
    wochentag = models.CharField(max_length=255, blank=True, null=True)
    startzeit = models.DateField(blank=True, null=True)
    trainerid = models.ForeignKey(Trainer, models.DO_NOTHING, db_column='trainerID', blank=True, null=True)  # Field name made lowercase.
    sportartid = models.ForeignKey(Sportarten, models.DO_NOTHING, db_column='sportartID', blank=True, null=True)  # Field name made lowercase.
    niveauid = models.ForeignKey(Leistungsniveaus, models.DO_NOTHING, db_column='niveauID', blank=True, null=True)  # Field name made lowercase.
    ortid = models.ForeignKey(Orte, models.DO_NOTHING, db_column='ortID', blank=True, null=True)  # Field name made lowercase.


class Zahlungen(models.Model):
    zahlungid = models.AutoField(db_column='zahlungID', primary_key=True)  # Field name made lowercase.
    datum = models.DateField()
    betrag = models.IntegerField()
    mitglied = models.ForeignKey(Mitglieder, models.DO_NOTHING, db_column='mitgliedID', blank=True, null=True)  # Field name made lowercase.
