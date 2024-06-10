import pickle

class CalendarioAllenamento:
    def __init__(self, giorno, ora_inizio, ora_fine, istruttore, corso):
        self.giorno = giorno
        self.ora_inizio = ora_inizio
        self.ora_fine = ora_fine
        self.istruttore = istruttore
        self.corso = corso

    def __str__(self):
        return (f" - {self.giorno}, dalle ore {self.ora_inizio} "
                f"alle ore {self.ora_fine} \nistruttore = {self.istruttore}")
