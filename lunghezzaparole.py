parole = []
lunghezza = []
n_parole = int(input("Quante parole vuoi inserire? "))

for n in range(1,n_parole+1):
    parola = str(input("Inserisci una parola \n"))
    parole.append(parola)
    l_parola= len(parola)
    lunghezza.append(l_parola)
    print("La lunghezza della parola ", parola," è ", l_parola)

risultato = zip(parole, lunghezza)
print("Ti fornisco i risultati finali: ", list(risultato))