print("Questo programma riconosce se, una parola passata dall'utente, si tratta o no di un palindromo")
print("Un palindromo è una parola che, se letta al contrario, ha lo stesso significato")
print()

parola = str(input("Inserisci una parola"))
palindromo = parola[::-1]
if parola == palindromo:
    print("La parola ", parola, " è un palindromo")
else:
    print("La parola ", parola, " non è un palindromo")