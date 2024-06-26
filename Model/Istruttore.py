import os.path
import pickle

class Istruttore:
    def __init__(self, nome, cognome, data_nascita, luogo_nascita, cf, telefono, livello):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.luogo_nascita = luogo_nascita
        self.cf = cf
        self.telefono = telefono
        self.livello = livello

    def is_valid(self):
        # Validate CF length and alphanumeric
        if len(self.cf) != 16 or not self.cf.isalnum():
            return False, "Codice fiscale deve essere di 16 caratteri alfanumerici."

        # Validate phone number length and numeric
        if len(self.telefono) != 10 or not self.telefono.isdigit():
            return False, "Numero di telefono deve essere di 10 cifre numeriche."

        return True, ""

    def ricercaIstruttore(cf):
        if os.path.isfile('Istruttori.pickle'):
            with open('Istruttori.pickle', 'rb') as f:
                istruttori = pickle.load(f)
                return istruttori.get(cf)
        return None

    def salvaIstruttore(self):
        valid, message = self.is_valid()
        if not valid:
            return False, message
        istruttori = {}
        if os.path.isfile('Istruttori.pickle'):
            with open('Istruttori.pickle', 'rb') as f:
                istruttori = pickle.load(f)

        istruttori[self.cf] = self
        try:
            with open('Istruttori.pickle', 'wb') as f:
                pickle.dump(istruttori, f, pickle.HIGHEST_PROTOCOL)
            return True
        except Exception as e:
            print(f"Errore durante il salvataggio dell'Istruttore: {e}")
            return False

    def rimuoviIstruttore(cf):
        if os.path.isfile('Istruttori.pickle'):
            with open('Istruttori.pickle', 'rb') as f:
                istruttori = pickle.load(f)

            if cf in istruttori:
                del istruttori[cf]

                try:
                    with open('Istruttori.pickle', 'wb') as f:
                        pickle.dump(istruttori, f, pickle.HIGHEST_PROTOCOL)
                    return True
                except Exception as e:
                    print(f"Errore durante la rimozione dell'Istruttore: {e}")
                    return False
            else:
                return False  # Istruttore non trovato
        else:
            print("Nessun file di dati trovato.")
            return False

    def get_lista_istruttori():
        istruttori_list = {}
        if os.path.isfile('Istruttori.pickle'):
            with open('Istruttori.pickle', 'rb') as f:
                try:
                    loaded_istruttori = pickle.load(f)
                    # Verify each loaded object
                    for key, istruttore in loaded_istruttori.items():
                        if isinstance(istruttore, Istruttore):
                            istruttori_list[key] = istruttore
                        else:
                            print(f"Object with key {key} is not an instance of Istruttore.")
                except Exception as e:
                    print(f"Error loading Istruttori.pickle: {e}")
        return istruttori_list

    def mostra_dettagli_Istruttore(self):
        print("Dettagli Istruttore:")
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Data di Nascita: {self.data_nascita}")
        print(f"Luogo di Nascita: {self.luogo_nascita}")
        print(f"Codice Fiscale: {self.cf}")
        print(f"Telefono: {self.telefono}")
