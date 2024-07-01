import tkinter as tk
from tkinter import ttk

from Controller.AbbonamentoController import AbbonamentoController
from Controller.AtletaController import AtletaController
from Controller.CorsoController import CorsoController
from Controller.GaraController import GaraController
from Controller.IstruttoreController import IstruttoreController
from Model.Abbonamento import Abbonamento
from Model.Atleta import Atleta
from Model.Corso import Corso
from Model.Gara import Gara
from Model.Istruttore import Istruttore
from View.Amministratore.AllenamentiView import AllenamentiView
from View.Amministratore.AtletaView import AtletaView
from View.Amministratore.GaraView import GestioneGareView
from View.Amministratore.IstruttoreView import IstruttoreView
from View.Amministratore.StatisticheView import StatisticheView


class HomeAmministratoreView:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Home Amministratore")

        self.abbonamento_controller = AbbonamentoController(Abbonamento, self)
        self.controller = AtletaController(Atleta, self, self.abbonamento_controller)
        self.gara_controller = GaraController(Gara)

        self.create_widgets()

    def create_widgets(self):
        admin_frame = ttk.LabelFrame(self.master, text="Pannello di Amministrazione")
        admin_frame.grid(column=0, row=0, columnspan=2, sticky="nsew", padx=20, pady=20)

        buttons = [
            ("Gestione Atleti", self.manage_atleti),
            ("Gestione Istruttori", self.manage_istruttori),
            ("Gestione Allenamenti", self.manage_allenamenti),
            ("Gestione Gare", self.manage_gare),
            ("Visualizza Statistiche", self.manage_statistiche)
        ]

        for idx, (text, command) in enumerate(buttons):
            ttk.Button(admin_frame, text=text, command=command).grid(column=0, row=idx, sticky="ew", padx=10, pady=10)

    def manage_atleti(self):
        new_window = tk.Toplevel(self.master)
        abbonamento_controller = AbbonamentoController(Abbonamento, None)
        athlete_controller = AtletaController(Atleta, None, abbonamento_controller )
        athlete_app = AtletaView(new_window, athlete_controller)
        athlete_controller.view = athlete_app
        athlete_app.setup_gui()

    def manage_istruttori(self):
        new_window = tk.Toplevel(self.master)
        istruttore_controller = IstruttoreController(Istruttore, None)
        istruttore_app = IstruttoreView(new_window, istruttore_controller)
        istruttore_controller.view = istruttore_app
        istruttore_app.setup_gui()

    def manage_allenamenti(self):
        new_window = tk.Toplevel(self.master)
        allenamenti_controller = CorsoController(Corso)
        allenamenti_app = AllenamentiView(new_window, allenamenti_controller)
        allenamenti_controller.view = allenamenti_app


    def manage_gare(self):
        new_window = tk.Toplevel(self.master)
        gara_app = GestioneGareView(new_window, self.gara_controller, self.controller)
        self.gara_controller.view = gara_app
        gara_app.setup_gui()

    def manage_statistiche(self):
        new_window = tk.Toplevel(self.master)
        statistiche_app = StatisticheView(new_window)

# To use this class:
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeAmministratoreView(root)
    root.mainloop()