vocali = "aeiou"
while True:
    parola = input("\nInserisci il testo che desideri tradurre: ")
    traduzione = ""
    for lettera in parola: #per ogni lettera della parola
        if lettera in vocali: #se la lettera è una vocale
            traduzione = traduzione + lettera
        else: #se la lettera  è una consonante
            traduzione = traduzione + lettera + "o" + lettera

    print("La traduzione della parola ",parola," è:")
    print(traduzione)
    scelta = input("Desideri tradurre un altra parola? ")
    if scelta == "no":
        break