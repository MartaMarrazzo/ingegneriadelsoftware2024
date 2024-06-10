import os
import pickle
from tkinter import messagebox
from Model.Login import LoginModel

class LoginController:
    def __init__(self, view):
        self.view = view
        self.model = LoginModel()

    def admin_login(self, username, password):
        """Check hashed password and handle login."""
        if username == "admin" and self.model.hash_password(password) == self.model.stored_password_hash:
            return True, "Login amministratore riuscito!"
        else:
            return False, "Username o Password errati"

    def atleta_login(self, username, password):
        if self.model.verifica_credenziali(username, password):
            cf = self.model.get_cf_by_username(username)
            if cf:
                return True, cf
            else:
                return False, "Codice Fiscale non trovato per l'utente"
        else:
            return False, "Username o Password errati"

    def verifica_cf(self, cf):
        atleta = self.model.ricerca_atleta(cf)
        if atleta:
            self.view.show_registra_atleta(cf)
        else:
            messagebox.showerror("Errore", "Codice Fiscale non trovato")

    def registra(self, username, password, confirm_password, cf):
        if not self.model.username_disponibile(username):
            messagebox.showerror("Errore", "Username già utilizzato")
        elif password != confirm_password:
            messagebox.showerror("Errore", "Le password non coincidono")
        else:
            self.model.salva_credenziali(cf, username, password)
            messagebox.showinfo("Successo", "Registrazione completata")

    def handle_admin_login(self, username, password):
        success, message = self.admin_login(username, password)
        if success:
            messagebox.showinfo("Login Success", message)
            self.view.open_admin_homepage()
        else:
            messagebox.showerror("Errore Login", message)

    def handle_atleta_login(self, username, password):
        success, result = self.atleta_login(username, password)
        if success:
            messagebox.showinfo("Login Success", "Login atleta riuscito!")
            self.view.open_atleta_homepage(result)
        else:
            messagebox.showerror("Errore Login", result)
