from Model.Istruttore import Istruttore

class IstruttoreController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_all_istruttori(self):
        istruttori = self.model.get_lista_istruttori()
        self.view.display_istruttori(istruttori)

    def add_istruttore(self, istruttore_data):
        existing_istruttore = self.model.ricercaIstruttore(istruttore_data['cf'])
        if existing_istruttore:
            return False, "Un istruttore con questo codice fiscale esiste già."

        nuovo_istruttore = Istruttore(**istruttore_data)
        valid, message = nuovo_istruttore.is_valid()
        if not valid:
            return False, message
        if nuovo_istruttore.salvaIstruttore():
            return True, "Istruttore aggiunto con successo."
        else:
            return False, "Errore nell'aggiunta dell'istruttore."

    def remove_istruttore(self, istruttore):
        cf = istruttore.cf
        if self.model.rimuoviIstruttore(cf):
            return True, "Istruttore rimosso con successo."
        else:
            return False, "Errore nella rimozione dell'istruttore o istruttore non trovato."

    def get_istruttore_by_cf(self, cf):
        return self.model.ricercaIstruttore(cf)
