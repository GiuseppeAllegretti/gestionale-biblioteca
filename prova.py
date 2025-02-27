class Studente:
    oreSettimanali = 36

    def __init__(self, nome, cognome, corsoStudi):
        self.nome = nome
        self.cognome = cognome
        self.corsoStudi = corsoStudi
    
    def __str__(self):
        return f"{self.nome} {self.cognome} {self.corsoStudi}\nore settimanali: {self.oreSettimanali}"


studente1 = Studente ("giuseppe", "allegretti", "informatica")
studente2= Studente ("marta", "stannis", "scienze")

studente1.oreSettimanali +=4

print (studente1)
print (studente2)