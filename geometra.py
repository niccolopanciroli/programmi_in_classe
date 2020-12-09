scelta = str(input("Scegli di quale figura vuoi conoscere l'area tra quelle proposte: quadrato, rettangolo, triangolo, cerchio\n "))

import math
if scelta == "quadrato":
    lato = float(input("Inserisci il lato del quadrato "))

    areaquadrato= lato * lato
    print("L'area del quadrato è ", areaquadrato)

elif  scelta == "rettangolo":
    base = float(input("Inserisci la base del rettangolo "))
    altezza = float(input("Inserisci l'altezza del rettangolo "))

    arearettangolo= base * altezza
    print("L'area del rettangolo è ", arearettangolo)

elif scelta == "triangolo":
    base = float(input("Inserisci la base del triangolo "))
    altezza = float(input("Inserisci l'altezza del triangolo "))

    areatriangolo= (base * altezza)/2
    print("L'area del triangolo è ", areatriangolo)

elif scelta == "cerchio":
    raggio = float(input("Inserisci il raggio del cerchio "))
    areacerchio= (raggio* raggio)*math.pi
    print("L'area del cerchio è ", areacerchio)
else:
    print("Nessun codice disponibile per la scelta effettuata")