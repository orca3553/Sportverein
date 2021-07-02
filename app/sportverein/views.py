from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from .models import Mitglieder, Beitraege, Zahlungen, Ruhend
from datetime import date


# Create your views here.
# Diese Methode wird am Anfang geladen und leitet die Seite zur Vorlage weiter.
def index(request):
    mitglieder = Mitglieder.objects.all()
    beitraege = Beitraege.objects.all()
    daten = []

    if mitglieder.count() > 0:
        for mitglied in mitglieder:
            for beitrag in beitraege:
                alter = calculate_age(mitglied.gebdat)
                if alter <= int(beitrag.bisalter):
                    ruhendtext = ''
                    try:
                        ruhend = Ruhend.objects.filter(mitgliedid=mitglied).latest('startdat')
                        if ruhend.enddat is None:
                            ruhendtext = 'ruhend'
                        else:
                            ruhendtext = 'aktiv'
                    except Ruhend.DoesNotExist:
                        ruhendtext = 'aktiv'
                    try:
                        zahlung = Zahlungen.objects.filter(mitglied=mitglied).latest('datum')
                        daten.append({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                                      'betrag': beitrag.betrag, 'datum': zahlung.datum, 'ruhend': ruhendtext})
                    except Zahlungen.DoesNotExist:
                        daten.append({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                                      'betrag': beitrag.betrag, 'datum': "N/A", 'ruhend': 'ruhend'})
            # for beitrag in beitraegeQs:
            # for mitglied in mitgliedQs:
            #     zahlungen = []
            #     for zahlung in zahlungenQs:
            #         if zahlung.mitgliedid == mitglied:
            #             zahlungen.append(zahlung)
            #     zahlung = ()
            #     for item in zahlungen:
            #         zahlung = item
            #         if zahlung.datum < item.datum:
            #             zahlung = item
            #     alter = calculate_age(mitglied.gebdat)
            #     if alter <= int(beitrag.bisalter):
            #
            #         daten.append({'id': mitglied, 'vname': mitglied.vname, 'nname': mitglied.nname,
            #       'betrag': beitrag.betrag, 'datum': zahlung.datum})
    context = {
        'daten': daten,
    }
    return render(request, 'sportverein/index.html', context=context)


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def sportform(request: HttpRequest) -> HttpResponse:
    mitglieder = Mitglieder.objects.all()
    zahlungen = Zahlungen.objects.all()
    beitraege = Beitraege.objects.all()
    daten = []
    ruhendbool = False
    ruhend = ()

    if request.method == 'POST':
        for mitglied in mitglieder:
            betrag = ''
            for beitrag in beitraege:
                alter = calculate_age(mitglied.gebdat)
                if alter <= int(beitrag.bisalter):
                    betrag = beitrag.betrag

            try:
                ruhend = Ruhend.objects.filter(mitgliedid=mitglied).latest('startdat')
                if ruhend.enddat is None:
                    ruhendbool = True
                else:
                    ruhendbool = False
            except Ruhend.DoesNotExist:
                ruhendbool = False

            zahlungen = []
            for item in zahlungen:
                if item.mitgliedid == mitglied:
                    zahlungen.append(item)
            if zahlungen.__len__() > 0:
                zahlung = ()
                first = True
                for item in zahlungen:
                    if first:
                        zahlung = item
                    if zahlung.datum < item.datum:
                        zahlung = item

                value = request.POST.get("id_" + str(mitglied.mitgliedid))
                if value == 'on':
                    if ruhendbool:
                        end_Ruhend(ruhend)
                    data = ({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                             'betrag': betrag, 'datum': date.today(), 'ruhend': 'aktiv'})
                    save_Zahlung(betrag, mitglied)
                    daten.append(data)
                else:
                    if ruhendbool is False:
                        set_Ruhend(mitglied)
                    daten.append({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                                  'betrag': zahlung.betrag, 'datum': zahlung.datum, 'ruhend': 'ruhend'})
            else:
                value = request.POST.get("id_" + str(mitglied.mitgliedid))
                if value == 'on':
                    if ruhendbool:
                        end_Ruhend(ruhend)
                    data = ({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                             'betrag': betrag, 'datum': date.today(), 'ruhend': 'aktiv'})
                    save_Zahlung(betrag, mitglied)
                    daten.append(data)
                else:
                    if ruhendbool is False:
                        set_Ruhend(mitglied)
                    daten.append({'id': mitglied.mitgliedid, 'vname': mitglied.vname, 'nname': mitglied.nname,
                                  'betrag': betrag, 'datum': 'N/A', 'ruhend': 'ruhend'})

    template = loader.get_template('sportverein/index.html')
    context = {
        'daten': daten,
    }
    return HttpResponse(template.render(context, request))


def save_Zahlung(betrag, mitglied):
    zahlung = Zahlungen(datum=date.today(), betrag=betrag, mitglied=mitglied)
    zahlung.save()
    return


def set_Ruhend(mitglied):
    ruhend = Ruhend(startdat=date.today(), mitgliedid=mitglied)
    ruhend.save()
    return

def end_Ruhend(ruhend):
    ruhend.enddat = date.today()
    ruhend.save()
    return
