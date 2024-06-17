from Controller.AtletaController import AtletaController
from Model.Atleta import Atleta
from Model.Gara import Gara


class GaraController:
    def __init__(self, model):
        self.model = model
    "restitituisci tutte le gare"
    def get_gare(self):
        return self.model.get_gare()

    "genera nuova gara con nome diverso da gare già inserite"
    def crea_gara(self, nome, data, luogo, requisiti):
        existing_gara = self.get_gara_by_nome(nome)
        if existing_gara:
            return False, f"Una gara con il nome '{nome}' esiste già."

        nuova_gara = Gara(nome, data, luogo, requisiti)
        self.model.aggiungi_gara(nuova_gara)
        return True, "Gara creata con successo."
    "trova gara per nome"
    def get_gara_by_nome(self, nome):
        return self.model.ricerca_gara(nome)

    def add_participant(self, gara, cf):
        success, message = gara.aggiungi_partecipante(cf)
        if success:
            gara.save_partecipanti()
        return success, message

    "prenotazione di una gara per un atleta"
    def book_gara(self, gara_nome, partecipante_cf):
        gara = self.get_gara_by_nome(gara_nome)
        if gara:
            return self.add_participant(gara, partecipante_cf)
        else:
            return False, "Gara non trovata."

    "mostra le prenotazioni effettuate dal singolo atleta- x area atleta"
    def get_prenotazioni(self, cf):
        prenotazioni = []
        gare = self.get_gare()
        for gara in gare:
            if cf in gara.load_partecipanti():
                prenotazioni.append(gara)
        return prenotazioni
    "cancella la prenotazione di quell'atlteta ad una determinata gara"
    def delete_prenotazione(self, gara_nome, cf):
        gara = self.get_gara_by_nome(gara_nome)
        if gara and cf in gara.load_partecipanti():
            partecipanti = gara.load_partecipanti()
            partecipanti.remove(cf)
            gara.save_partecipanti()
            return True, "Prenotazione cancellata."
        return False, "Prenotazione non trovata o utente non iscritto."

    def get_prenotazioni_gara(self, gara_nome):
        gara = self.get_gara_by_nome(gara_nome)
        if gara:
            return gara.load_partecipanti()

    def get_atleta_by_cf(self,cf):
        return Atleta.ricercaAtleta(cf)

    def save_result(self, gara, cf, risultato):
        return gara.registra_risultato(cf, risultato)
