import hashlib
import os
import pickle

class LoginModel:
    def __init__(self):
        self.stored_password_hash = self.hash_password("admin")

    def hash_password(self, password):
        """Hash a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verifica_credenziali(self, username, password):
        if os.path.isfile('Credenziali.pickle'):
            with open('Credenziali.pickle', 'rb') as f:
                credenziali = pickle.load(f)
                if username in credenziali and credenziali[username]['password'] == self.hash_password(password):
                    return True
        return False

    def ricerca_atleta(self, cf):
        if os.path.isfile('Atleti.pickle'):
            with open('Atleti.pickle', 'rb') as f:
                atleti = pickle.load(f)
                return atleti.get(cf)
        return None

    def username_disponibile(self, username):
        if os.path.isfile('Credenziali.pickle'):
            with open('Credenziali.pickle', 'rb') as f:
                credenziali = pickle.load(f)
                return username not in credenziali
        return True

    def salva_credenziali(self, cf, username, password):
        credenziali = {}
        if os.path.isfile('Credenziali.pickle'):
            with open('Credenziali.pickle', 'rb') as f:
                credenziali = pickle.load(f)

        credenziali[username] = {
            'password': self.hash_password(password),
            'cf': cf
        }

        with open('Credenziali.pickle', 'wb') as f:
            pickle.dump(credenziali, f, pickle.HIGHEST_PROTOCOL)

    def get_cf_by_username(self, username):
        if os.path.isfile('Credenziali.pickle'):
            with open('Credenziali.pickle', 'rb') as f:
                credenziali = pickle.load(f)
                return credenziali.get(username, {}).get('cf')
        return None
