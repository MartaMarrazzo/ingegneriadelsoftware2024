import os
import pickle
from datetime import datetime
class Gara:
    def __init__(self, nome, data, luogo, requisiti):
        self.nome = nome
        self.data = data
        self.luogo = luogo
        self.requisiti = requisiti
        self.partecipanti = self.load_partecipanti()
        self.risultati = self.load_risultati()

    def aggiungi_partecipante(self, partecipante_cf):
        self.partecipanti = self.load_partecipanti()
        if partecipante_cf not in self.partecipanti:
            self.partecipanti.append(partecipante_cf)
            self.save_partecipanti()
            return True, "Partecipante aggiunto alla gara."
        else:
            return False, "Il partecipante è già registrato."

    def registra_risultato(self, partecipante_cf, risultato):
        self.partecipanti = self.load_partecipanti()
        print(f"Checking if {partecipante_cf} is in {self.partecipanti}")  # Debug statement
        if partecipante_cf in self.partecipanti:
            self.risultati[partecipante_cf] = risultato
            self.save_risultati()
            return True, "Risultato registrato."
        else:
            return False, "Il partecipante non è registrato alla gara."

    @staticmethod
    def get_gare():
        if os.path.isfile('Dati/Gare.pickle'):
            with open('Dati/Gare.pickle', 'rb') as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return []
        return []

    def ricerca_gara(nome):
        if os.path.isfile('Dati/Gare.pickle'):
            with open('Dati/Gare.pickle', 'rb') as f:
                try:
                    gare = pickle.load(f)
                    for gara in gare:
                        if gara.nome == nome:
                            return gara
                except EOFError:
                    return None
        return None

    def salva_gare(gare):
        with open('Dati/Gare.pickle', 'wb') as f:
            pickle.dump(gare, f, pickle.HIGHEST_PROTOCOL)

    def aggiungi_gara(gara):
        gare = Gara.get_gare()
        gare.append(gara)
        Gara.salva_gare(gare)

    def save_partecipanti(self):
        file_path = f'Dati/Partecipanti_{self.nome}.pickle'
        with open(file_path, 'wb') as f:
            pickle.dump(self.partecipanti, f, pickle.HIGHEST_PROTOCOL)

    def load_partecipanti(self):
        file_path = f'Dati/Partecipanti_{self.nome}.pickle'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return []
        return []

    def save_risultati(self):
        file_path = f'Dati/Risultati_{self.nome}.pickle'
        with open(file_path, 'wb') as f:
            pickle.dump(self.risultati, f, pickle.HIGHEST_PROTOCOL)

    def load_risultati(self):
        file_path = f'Dati/Risultati_{self.nome}.pickle'
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as f:
                try:
                    return pickle.load(f)
                except EOFError:
                    return {}
        return {}

    def get_all_risultati():
        gare = Gara.get_gare()
        all_risultati = {}
        for gara in gare:
            all_risultati[gara.nome] = gara.load_risultati()
        return all_risultati

