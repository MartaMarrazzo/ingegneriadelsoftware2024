import tkinter as tk
from tkinter import ttk, messagebox

from Controller.AbbonamentoController import AbbonamentoController
from Controller.CorsoController import CorsoController
from Controller.GaraController import GaraController
from Model.Abbonamento import Abbonamento
from Model.Corso import Corso
from Model.Gara import Gara
from View.Home.HomeAmministratoreView import HomeAmministratoreView
from View.Home.HomeAtletaView import HomeAtletaView


class HomePageView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        master.title("Homepage")
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabelFrame', font=('Helvetica', 12, 'bold'), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 10), background='pink', foreground='black')
        self.style.configure('TEntry', font=('Helvetica', 10), padding=5, background='white')
        self.style.configure('TCombobox', font=('Helvetica', 10), padding=5, background='white', foreground='black')
        self.style.configure('Treeview', font=('Helvetica', 10), rowheight=25)
        self.style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.create_widgets()

    def create_widgets(self):
        # Buttons for atleta and amministratore
        ttk.Button(self.master, text="Atleta", command=self.open_atleta_options).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.master, text="Amministratore", command=self.open_admin_login).grid(row=0, column=1, padx=10, pady=10)

    def open_atleta_options(self):
        atleta_window = tk.Toplevel(self.master)
        atleta_window.title("Opzioni Atleta")

        ttk.Button(atleta_window, text="Login", command=self.atleta_login).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(atleta_window, text="Registrazione", command=self.atleta_registrazione).grid(row=1, column=0, padx=10, pady=10)

    def open_admin_login(self):
        admin_window = tk.Toplevel(self.master)
        admin_window.title("Login Amministratore")

        ttk.Label(admin_window, text="Username:").grid(row=0, column=0)
        username_entry = ttk.Entry(admin_window)
        username_entry.grid(row=0, column=1)

        ttk.Label(admin_window, text="Password:").grid(row=1, column=0)
        password_entry = ttk.Entry(admin_window, show="*")
        password_entry.grid(row=1, column=1)

        ttk.Button(admin_window, text="Login", command=lambda: self.controller.handle_admin_login(username_entry.get(), password_entry.get())).grid(row=2, column=1)

    def handle_atleta_login(self, username, password):
        success, result = self.controller.atleta_login(username, password)
        if success:
            messagebox.showinfo("Login Success", "Login atleta riuscito!")
            self.open_atleta_homepage(result)
        else:
            messagebox.showerror("Errore Login", result)

    def atleta_registrazione(self):
        atleta_window = tk.Toplevel(self.master)
        atleta_window.title("Registrazione Atleta")

        tk.Label(atleta_window, text="Codice Fiscale:").grid(row=0, column=0)
        cf_entry = ttk.Entry(atleta_window)
        cf_entry.grid(row=0, column=1)

        ttk.Button(atleta_window, text="Verifica", command=lambda: self.controller.verifica_cf(cf_entry.get())).grid(row=1, column=1)

    def show_registra_atleta(self, cf):
        parent_window = tk.Toplevel(self.master)
        parent_window.title("Scelta Username e Password")

        tk.Label(parent_window, text="Username:").grid(row=0, column=0)
        username_entry = ttk.Entry(parent_window)
        username_entry.grid(row=0, column=1)

        tk.Label(parent_window, text="Password:").grid(row=1, column=0)
        password_entry = ttk.Entry(parent_window, show="*")
        password_entry.grid(row=1, column=1)

        tk.Label(parent_window, text="Conferma Password:").grid(row=2, column=0)
        confirm_password_entry = ttk.Entry(parent_window, show="*")
        confirm_password_entry.grid(row=2, column=1)

        ttk.Button(parent_window, text="Registrati", command=lambda: self.controller.registra(username_entry.get(), password_entry.get(), confirm_password_entry.get(), cf)).grid(row=3, column=1)

    def atleta_login(self):
        atleta_window = tk.Toplevel(self.master)
        atleta_window.title("Login Atleta")

        tk.Label(atleta_window, text="Username:").grid(row=0, column=0)
        username_entry = ttk.Entry(atleta_window)
        username_entry.grid(row=0, column=1)

        tk.Label(atleta_window, text="Password:").grid(row=1, column=0)
        password_entry = ttk.Entry(atleta_window, show="*")
        password_entry.grid(row=1, column=1)

        ttk.Button(atleta_window, text="Login", command=lambda: self.controller.handle_atleta_login(username_entry.get(), password_entry.get())).grid(row=2, column=1)

    def open_admin_homepage(self):
        new_window = tk.Toplevel(self.master)
        app = HomeAmministratoreView(new_window)

    def open_atleta_homepage(self, cf):
        new_window = tk.Toplevel(self.master)

        # Instantiate the controllers
        gara_controller = GaraController(Gara, new_window)
        corso_controller = CorsoController(Corso)
        abbonamento_controller = AbbonamentoController(Abbonamento, new_window)

        # Create the HomeAtletaView and pass the controllers to it
        app = HomeAtletaView(new_window, gara_controller, corso_controller, abbonamento_controller, cf)

        # Optionally, set the view attribute of each controller if they need to interact with the view
        gara_controller.view = app
        corso_controller.view = app
        abbonamento_controller.view = app