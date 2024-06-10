from Model.CalendarioAllenamenti import CalendarioAllenamento
from Model.Corso import Corso

class CorsoController:
    def __init__(self, model):
        self.model = model

    def get_corso_by_nome(self, nome_corso):
        return self.model.ricerca_corso(nome_corso)

    def aggiungi_corso(self, nome_corso, descrizione, istruttori, giorno, ora_inizio, ora_fine,giorno2, ora_inizio2, ora_fine2):
        nuovo_corso = Corso(nome_corso=nome_corso, descrizione=descrizione, istruttori=istruttori)
        allenamento = CalendarioAllenamento(giorno=giorno, ora_inizio=ora_inizio, ora_fine=ora_fine,
                                            istruttore=istruttori, corso=nome_corso)
        allenamento2 = CalendarioAllenamento(giorno=giorno2, ora_inizio=ora_inizio2, ora_fine=ora_fine2,
                                            istruttore=istruttori, corso=nome_corso)
        nuovo_corso.aggiungi_allenamento(allenamento)
        nuovo_corso.aggiungi_allenamento(allenamento2)

        self.model.aggiungi_corso(nuovo_corso)

    def elimina_corso(self, nome_corso):
        self.model.elimina_corso(nome_corso)
        if self.view:
            self.view.aggiorna_lista_corsi()

    def get_all_allenamenti(self):
        corsi = self.model.get_corsi()
        allenamenti = []
        for corso in corsi:
            allenamenti.extend(corso.calendario)
        return allenamenti
