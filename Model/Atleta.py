import os.path
import pickle
from datetime import datetime


class Atleta:
    def __init__(self, nome, cognome, data_nascita, luogo_nascita, cf, telefono, livello_atleta, tipo_abbonamento, cf_genitore, pagamento_assicurazione, scadenza_certificato_medico):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.cf = cf
        self.telefono = telefono
        self.livello_atleta = livello_atleta
        self.tipo_abbonamento = tipo_abbonamento
        self.cf_genitore = cf_genitore
        self.pagamento_assicurazione = pagamento_assicurazione
        self.scadenza_certificato_medico = scadenza_certificato_medico

    def is_valid(self):

        if not all([self.cf, self.telefono,self.tipo_abbonamento, self.scadenza_certificato_medico,
                    self.nome, self.pagamento_assicurazione, self.data_nascita, self.luogo_nascita,
                    self.cognome, self.livello_atleta]):
            return False, "Tutti i campi devono essere compilati."

        # Validate CF length and alphanumeric
        if len(self.cf) != 16 or not self.cf.isalnum():
            return False, "Codice fiscale deve essere di 16 caratteri alfanumerici."

        # Validate phone number length and numeric
        if len(self.telefono) != 10 or not self.telefono.isdigit():
            return False, "Numero di telefono deve essere di 10 cifre numeriche."
        if isinstance(self.data_nascita, str):
            try:
                self.data_nascita = datetime.strptime(self.data_nascita, "%Y-%m-%d")
            except ValueError:
                return False, "Il campo data_nascita deve essere nel formato YYYY-MM-DD."

            # Verifica e conversione per scadenza_certificato_medico
        if isinstance(self.scadenza_certificato_medico, str):
            try:
                self.scadenza_certificato_medico = datetime.strptime(self.scadenza_certificato_medico, "%Y-%m-%d")
            except ValueError:
                return False, "Il campo scadenza_certificato_medico deve essere nel formato YYYY-MM-DD."

            # Calculate age and validate minor's parent CF
        today = datetime.now()
        age = today.year - self.data_nascita.year - (
                    (today.month, today.day) < (self.data_nascita.month, self.data_nascita.day))
        if age < 18:
            if not self.cf_genitore or len(self.cf_genitore) != 16 or not self.cf_genitore.isalnum():
                return False, "Per gli atleti minorenni, il codice fiscale del genitore deve essere valido e non può essere vuoto."

        return True, ""

    def ricercaAtleta(cf):
        if os.path.isfile('Atleti.pickle'):
            with open('Atleti.pickle', 'rb') as f:
                atleti = pickle.load(f)
                return atleti.get(cf)
        return None

    def aggiornaAtleta(self, **updated_data):
        for key, value in updated_data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        valid, message = self.is_valid()
        if not valid:
            return False, message

        return self.salvaAtleta()  # Ensure salvaAtleta returns True/False

    def salvaAtleta(self):
        valid, message = self.is_valid()
        if not valid:
            return False, message
        atleti = {}
        if os.path.isfile('Atleti.pickle'):
            with open('Atleti.pickle', 'rb') as f:
                atleti = pickle.load(f)

        atleti[self.cf] = self
        try:
            with open('Atleti.pickle', 'wb') as f:
                pickle.dump(atleti, f, pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"Errore durante il salvataggio dell'atleta: {e}")
            return False

    @staticmethod
    def rimuoviAtleta(cf):
        if os.path.isfile('Atleti.pickle'):
            with open('Atleti.pickle', 'rb') as f:
                atleti = pickle.load(f)

            if cf in atleti:
                del atleti[cf]

                try:
                    with open('Atleti.pickle', 'wb') as f:
                        pickle.dump(atleti, f, pickle.HIGHEST_PROTOCOL)
                    return True
                except Exception as e:
                    print(f"Errore durante la rimozione dell'atleta: {e}")
                    return False
            else:
                return False  # Atleta non trovato
        else:
            print("Nessun file di dati trovato.")
            return False

    @staticmethod
    def get_lista_atleti():
        atleti = {}
        if os.path.isfile('Atleti.pickle'):
            with open('Atleti.pickle', 'rb') as f:
                try:
                    loaded_atleti = pickle.load(f)
                    # Verify each loaded object
                    for key, atleta in loaded_atleti.items():
                        if isinstance(atleta, Atleta):
                            atleti[key] = atleta
                        else:
                            print(f"Object with key {key} is not an instance of Atleta.")
                except Exception as e:
                    print(f"Error loading Atleti.pickle: {e}")
        return atleti

    def mostra_dettagli_atleta(self):
        print("Dettagli Atleta:")
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Data di Nascita: {self.data_nascita}")
        print(f"Luogo di Nascita: {self.luogo_nascita}")
        print(f"Codice Fiscale: {self.cf}")
        print(f"Telefono: {self.telefono}")
        print(f"Livello Atleta: {self.livello_atleta}")
        print(f"Tipo di Abbonamento: {self.tipo_abbonamento}")
        print(f"Codice Fiscale Genitore (se applicabile): {self.cf_genitore if self.cf_genitore else 'N/A'}")
        print(f"Pagamento Assicurazione: {'Sì' if self.pagamento_assicurazione else 'No'}")
        print(f"Scadenza Certificato Medico: {self.scadenza_certificato_medico}")
