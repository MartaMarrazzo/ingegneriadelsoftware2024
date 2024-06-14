
from Model.Atleta import Atleta


class AtletaController:
    def __init__(self, model, view, abbonamento_controller):
        self.model = model
        self.view = view
        self.abbonamento_controller = abbonamento_controller

    def display_all_atleti(self):
        atleti = self.model.get_lista_atleti()
        self.view.display_atleti(atleti)

    def add_atleta(self, atleta_data):
        existing_atleta = self.model.ricercaAtleta(atleta_data['cf'])
        if existing_atleta:
            return False, "Un atleta con questo codice fiscale esiste già."

        nuovo_atleta = Atleta(**atleta_data)
        valid, message = nuovo_atleta.is_valid()
        if not valid:
            return False, message
        if nuovo_atleta.salvaAtleta():
            return True, "Atleta aggiunto con successo."
        else:
            return False, "Errore nell'aggiunta dell'atleta."

    def remove_atleta(self, atleta,top):
        cf = atleta.cf
        if self.model.rimuoviAtleta(cf):
            self.view.show_message("Atleta rimosso con successo.")
        else:
            self.view.show_message("Errore nella rimozione dell'atleta o atleta non trovato.")
        top.destroy()

    def update_atleta2(self, atleta, updated_data,top):
        if atleta:
            if atleta.aggiornaAtleta(**updated_data):
                valid, message = atleta.is_valid()
                if not valid:
                    return False, message
                return True, "Atleta updated successfully"
            else:
                self.view.show_message("Controller : Errore nell'aggiornamento dell'atleta.")
        else:
            self.view.show_message("Controller :Atleta non trovato.")
        top.destroy()

    def get_atleta_by_cf(self,cf):
       return self.model.ricercaAtleta(cf)
