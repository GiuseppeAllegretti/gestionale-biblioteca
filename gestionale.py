import json

# implemento la classe Libro e definisco metodi e attributi
class Libro:
    contatore_id = 0

    def __init__(self, titolo, autore):
        Libro.contatore_id += 1
        self.id = Libro.contatore_id
        self.titolo = titolo
        self.autore = autore

    def __str__(self):
        return f"ID: {self.id}| {self.titolo} di {self.autore}"
    
# implemento la classe Utente e definisco metodi e attributi
class Utente:
    def __init__(self, username, nome, cognome):
        self.username = username
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return f"Username: {self.username} | {self.nome} {self.cognome}"

# implemento la classe Biblioteca e definisco metodi e attributi
class Biblioteca:
    def __init__(self):
        # creo dei dizionari vuoti che conterranno gli utenti e i libri inseriti dall'utente
        self.libriDisponibili = {} 
        self.utenti = {}

        self.caricaDati() 

# aggiunta nuovo libro
    def aggiungiLibro (self):
        titolo = input ("Titolo: ")
        autore = input ("Autore: ")

        libro = Libro (titolo, autore) # creo l'oggetto libro con asssegnando i parametri presi dall'imput dell'utente
        self.libriDisponibili[libro.id] = libro # aggiungo id del nuovo oggetto creato al dizionario
        self.salvaDati()
        print ("Libro aggiunto in biblioteca!\n")
                
# visualizziamo l'elenco dei libri aggiunti
    def elencoLibri (self):
        for libro in self.libriDisponibili.values (): # passo in rassegna tutti i valori dei libri nel dizionario e li stampo
            print (libro)

# aggiunta nuovo utente
    def aggiungiUtente (self):
        nome = input ("Nome: ").strip().upper()
        cognome = input ("Cognome: ").strip().upper()
        username = input ("Scegli la tua Username: ")

# controllo che l'utente non sia gia presente nel dict
        for utente in self.utenti.values():
            if utente.nome.strip().upper() == nome and utente.cognome.strip().upper() == cognome:
                print ("Utente gia registrato con questo nome...")
                return
        if username in self.utenti:
            print ("Username già in uso... Scegline un'altra")
            return

        # altrimenti creo l'oggetto utente con i parametri, e li aggiungo al dizionario con username come chiave
        utente = Utente(username, nome, cognome)
        self.utenti[username] = utente
        self.salvaDati ()
        print("Utente aggiunto con successo...\n")

# salvo i dati utilizzando json
    def salvaDati (self):
        with open ("dati_biblioteca.json", "w") as file: # apro o creo il file in modalita scrittura
            # scrivo i dati (chiave/valore) presi dal dizionario all'interno di un dizionario nel file json 
            json.dump ({
                "libri": {id: {"titolo": libro.titolo, "autore": libro.autore} for id, libro in self.libriDisponibili.items()},
                "utenti": {username: {"nome": utente.nome, "cognome": utente.cognome} for username, utente in self.utenti.items()}
            }, file, indent = 4)

# carico i dati nel file json
    def caricaDati (self):
        try:
            with open ("dati_biblioteca.json", "r") as file: # apro il file in modalita lettura
                dati = json.load(file)
                self.libriDisponibili = {int(id): Libro (d["titolo"], d["autore"]) for id, d in dati["libri"].items()}
                self.utenti = {username: Utente(username, d["nome"], d["cognome"] ) for username, d in dati["utenti"].items()}
        except(FileNotFoundError, json.JSONDecodeError):
            print ("Nessun dato salvato trovato, biblioteca vuota...")



# visualizziamo l'elenco degli Utenti aggiunti
    def elencoUtenti (self):
        if not self.utenti: # se il dizionario è vuoto stampa messaggio
            print ("Nessun utente registrato")
        else: # altrimenti passa in rassegna tutti i valori del dizionario e me li stampa
            for utente in self.utenti.values ():
                print (utente)
        
#rimozione utente
    def rimuoviUtente (self):
            userDaRimuovere = input ("Inserisci la username corrispondente all'utente che vuoi cancellare -> ")
            
            if userDaRimuovere in self.utenti: # se l'id preso dall'input è presente nel dizionario utenti, viene rimosso 
                del self.utenti[userDaRimuovere]
                self.salvaDati ()
                print ("Utente rimosso con successo...")
                return
            else:
                print ("Non è presente un utente con questa Username...\nInserisci la Username corretta")
