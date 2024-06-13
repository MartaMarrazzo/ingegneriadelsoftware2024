from idlelib import window

from Model.Corso import Corso
import tkinter as tk
from tkinter import ttk, messagebox


class AggiungiCorsoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Aggiungi Corso")

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10)

        self.nome_label = ttk.Label(self.frame, text="Nome Corso:")
        self.nome_label.grid(row=0, column=0, sticky="w")
        self.nome_entry = ttk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        self.descrizione_label = ttk.Label(self.frame, text="Descrizione:")
        self.descrizione_label.grid(row=1, column=0, sticky="w")
        self.descrizione_entry = ttk.Entry(self.frame)
        self.descrizione_entry.grid(row=1, column=1)

        self.istruttori_label = ttk.Label(self.frame, text="Istruttori:")
        self.istruttori_label.grid(row=2, column=0, sticky="w")
        self.istruttori_entry = ttk.Entry(self.frame)
        self.istruttori_entry.grid(row=2, column=1)

        self.giorno_label = ttk.Label(self.frame, text="Giorno:")
        self.giorno_label.grid(row=3, column=0, sticky="w")
        self.giorno_entry = ttk.Entry(self.frame)
        self.giorno_entry.grid(row=3, column=1)

        self.ora_inizio_label = ttk.Label(self.frame, text="Ora Inizio:")
        self.ora_inizio_label.grid(row=4, column=0, sticky="w")
        self.ora_inizio_entry = ttk.Entry(self.frame)
        self.ora_inizio_entry.grid(row=4, column=1)

        self.ora_fine_label = ttk.Label(self.frame, text="Ora Fine:")
        self.ora_fine_label.grid(row=5, column=0, sticky="w")
        self.ora_fine_entry = ttk.Entry(self.frame)
        self.ora_fine_entry.grid(row=5, column=1)

        self.giorno2_label = ttk.Label(self.frame, text="Giorno:")
        self.giorno2_label.grid(row=6, column=0, sticky="w")
        self.giorno2_entry = ttk.Entry(self.frame)
        self.giorno2_entry.grid(row=6, column=1)

        self.ora_inizio2_label = ttk.Label(self.frame, text="Ora Inizio:")
        self.ora_inizio2_label.grid(row=7, column=0, sticky="w")
        self.ora_inizio2_entry = ttk.Entry(self.frame)
        self.ora_inizio2_entry.grid(row=7, column=1)

        self.ora_fine2_label = ttk.Label(self.frame, text="Ora Fine:")
        self.ora_fine2_label.grid(row=8, column=0, sticky="w")
        self.ora_fine2_entry = ttk.Entry(self.frame)
        self.ora_fine2_entry.grid(row=8, column=1)

        self.aggiungi_button = ttk.Button(self.frame, text="Aggiungi", command=self.aggiungi_corso)
        self.aggiungi_button.grid(row=9, columnspan=2, pady=5)

    def aggiungi_corso(self):
        nome = self.nome_entry.get()
        descrizione = self.descrizione_entry.get()
        istruttori = self.istruttori_entry.get()
        giorno = self.giorno_entry.get()
        ora_inizio = self.ora_inizio_entry.get()
        ora_fine = self.ora_fine_entry.get()
        giorno2 = self.giorno2_entry.get()
        ora_inizio2 = self.ora_inizio2_entry.get()
        ora_fine2 = self.ora_fine2_entry.get()

        self.controller.aggiungi_corso(nome, descrizione, istruttori, giorno, ora_inizio, ora_fine, giorno2, ora_inizio2, ora_fine2)
        self.destroy()

class EliminaCorsoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Elimina Corso")

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10)

        self.nome_label = ttk.Label(self.frame, text="Nome Corso:")
        self.nome_label.grid(row=0, column=0, sticky="w")

        self.corsi = self.controller.get_all_corsi()
        self.nome_var = tk.StringVar()
        self.nome_combobox = ttk.Combobox(self.frame, textvariable=self.nome_var, values=self.corsi)
        self.nome_combobox.grid(row=0, column=1)

        self.elimina_button = ttk.Button(self.frame, text="Elimina", command=self.elimina_corso)
        self.elimina_button.grid(row=1, columnspan=2, pady=5)

    def elimina_corso(self):
        nome = self.nome_var.get()
        self.controller.elimina_corso(nome)
        tk.Toplevel.destroy(self)


class DettagliCorsoView(tk.Toplevel):
    def __init__(self, master, corso):
        super().__init__(master)
        self.title("Dettagli Corso")

        self.corso = corso

        self.dettagli_frame = ttk.Frame(self)
        self.dettagli_frame.pack(padx=10, pady=10)

        ttk.Label(self.dettagli_frame, text=f"Corso: {corso.nome_corso}").grid(row=0, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Descrizione: {corso.descrizione}").grid(row=1, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Giorni:").grid(row=3, column=0, sticky="w")
        for i, giorno in enumerate(corso.calendario):
            ttk.Label(self.dettagli_frame, text=f"  {giorno}").grid(row=4 + i, column=0, sticky="w")

class AllenamentiView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title('AllenamentiView')

        self.allenamenti_frame = ttk.LabelFrame(self.master, text="Allenamenti", padding=10)
        self.allenamenti_frame.grid(column=0, row=0, columnspan=2, sticky="ew", padx=10, pady=10)

        self.elenco_corsi_label = ttk.Label(self.allenamenti_frame, text="Elenco Corsi:")
        self.elenco_corsi_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")

        self.elenco_corsi_listbox = tk.Listbox(self.allenamenti_frame, width=50, height=10)
        self.elenco_corsi_listbox.grid(column=0, row=1, padx=5, pady=5)
        self.elenco_corsi_listbox.bind("<Double-Button-1>", self.mostra_dettagli_corso)

        self.aggiungi_button = ttk.Button(self.master, text="Aggiungi Corso", command=self.apri_aggiungi_corso)
        self.aggiungi_button.grid(column=0, row=2, padx=5, pady=5)

        self.elimina_button = ttk.Button(self.master, text="Elimina Corso", command=self.apri_elimina_corso)
        self.elimina_button.grid(column=1, row=2, padx=5, pady=5)

        self.calendario_label = ttk.Label(self.allenamenti_frame, text="Calendario:")
        self.calendario_label.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        self.calendario_listbox = tk.Listbox(self.allenamenti_frame, width=50, height=10)
        self.calendario_listbox.grid(column=1, row=1, padx=5, pady=5)

        self.aggiorna_lista_corsi()

    def aggiorna_lista_corsi(self):
        self.elenco_corsi_listbox.delete(0, tk.END)
        elenco_corsi = Corso.get_corsi()
        for corso in elenco_corsi:
            self.elenco_corsi_listbox.insert(tk.END, f"{corso.nome_corso}: {corso.descrizione}")
        self.aggiorna_calendario(elenco_corsi)

    def aggiorna_calendario(self, elenco_corsi):
        self.calendario_listbox.delete(0, tk.END)
        allenamenti_per_giorno = {}
        for corso in elenco_corsi:
            for allenamento in corso.calendario:
                if allenamento.giorno not in allenamenti_per_giorno:
                    allenamenti_per_giorno[allenamento.giorno] = []
                allenamenti_per_giorno[allenamento.giorno].append(allenamento)

        for giorno in sorted(allenamenti_per_giorno.keys()):
            self.calendario_listbox.insert(tk.END, f"Giorno: {giorno}")
            for allenamento in allenamenti_per_giorno[giorno]:
                self.calendario_listbox.insert(tk.END,
                                               f"  {allenamento.ora_inizio} - {allenamento.ora_fine}: {allenamento.corso} con {allenamento.istruttore}")

    def mostra_dettagli_corso(self, event):
        selection_index = self.elenco_corsi_listbox.curselection()
        if selection_index:
            index = selection_index[0]
            nome_corso = self.elenco_corsi_listbox.get(index).split(":")[0]
            corso = self.controller.get_corso_by_nome(nome_corso)
            if corso:
                dettagli_view = DettagliCorsoView(self.master, corso)
                dettagli_view.grab_set()
                dettagli_view.focus_set()
                dettagli_view.wait_window()

    def apri_aggiungi_corso(self):
        aggiungi_corso_view = AggiungiCorsoView(self.master, self.controller)
        aggiungi_corso_view.grab_set()
        aggiungi_corso_view.focus_set()
        aggiungi_corso_view.wait_window()

    def apri_elimina_corso(self):
        elimina_corso_view = EliminaCorsoView(self.master, self.controller)