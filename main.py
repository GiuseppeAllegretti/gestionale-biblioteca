from gestionale import Libro, Utente, Biblioteca
from colorama import Fore

biblioteca = Biblioteca ()

while True:
    print (Fore.MAGENTA)
    print (" \n📚 MENU 📚")
    print ("1- Aggiungi Libro 📕")
    print ("2- Aggiungi Utente 👥")
    print ("3- Visualizza libri disponibili 📖")
    print ("4- Visualizza elenco utenti 📖👥")
    print ("5- Rimuovi Utente ❌")
    print ("6- Esci... 👋")

    try:
        scelta = int(input("Fai la tua scelta (1-6) -> "))
        if scelta == 1:
            biblioteca.aggiungiLibro()
        elif scelta == 2:
            biblioteca.aggiungiUtente()
        elif scelta == 3:
            print ("\nLibri disponibini in Biblioteca")
            biblioteca.elencoLibri()
        elif scelta == 4:
            biblioteca.elencoUtenti()
        elif scelta == 5:
            biblioteca.rimuoviUtente()
        elif scelta == 6:
            break
        
    except ValueError:
        print ("Scelta errata... Riprova\n")
