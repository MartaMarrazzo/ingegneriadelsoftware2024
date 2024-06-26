import os
import pickle

class Corso:
    def __init__(self, nome_corso, descrizione, istruttori):
        self.nome_corso = nome_corso
        self.descrizione = descrizione
        self.istruttori = istruttori
        self.calendario = []

    def aggiungi_allenamento(self, allenamento):
        self.calendario.append(allenamento)

    def ricerca_corso(nome_corso):
        if os.path.isfile('Corsi.pickle'):
            with open('Corsi.pickle', 'rb') as f:
                try:
                    corsi = pickle.load(f)
                    for corso in corsi:
                        if corso.nome_corso == nome_corso:
                            return corso
                except EOFError:
                    return None
        return None

    @staticmethod
    def get_corsi():
        if os.path.isfile('Corsi.pickle'):
            with open('Corsi.pickle', 'rb') as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return []
        return []

    def salva_corsi(corsi):
        with open('Corsi.pickle', 'wb') as f:
            pickle.dump(corsi, f, pickle.HIGHEST_PROTOCOL)

    def aggiungi_corso(corso):
        corsi = Corso.get_corsi()
        corsi.append(corso)
        Corso.salva_corsi(corsi)

    def elimina_corso(nome_corso):
        corsi = Corso.get_corsi()
        corsi = [corso for corso in corsi if corso.nome_corso != nome_corso]
        Corso.salva_corsi(corsi)
