import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox

from View.Amministratore.InserisciRisultatiView import InserisciRisultatiView
class GestioneGaraView:
    def __init__(self, master, gara_controller, gara):
        self.master = master
        self.controller = gara_controller
        self.gara = gara
        self.master.title("Gestione Gara")
        self.setup_gui()
        self.update_iscritti_list()
        self.update_risultati_list()

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        iscritti_frame = ttk.LabelFrame(self.frame, text="Iscritti")
        iscritti_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.iscritti_listbox = tk.Listbox(iscritti_frame)
        self.iscritti_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        ttk.Button(iscritti_frame, text="Iscrivi Atleta", command=self.iscrivi_atleta).pack(side=tk.LEFT, padx=5, pady=5)

        risultati_frame = ttk.LabelFrame(self.frame, text="Risultati")
        risultati_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.risultati_listbox = tk.Listbox(risultati_frame)
        self.risultati_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.aggiungi_button = ttk.Button(risultati_frame, text="Aggiungi Risultato", command=self.aggiungi_risultato)
        self.aggiungi_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.check_date_and_toggle_button()

    def check_date_and_toggle_button(self):
        data_gara = self.gara.data# Convert data_gara to datetime
        oggi = datetime.now()

        if oggi > data_gara:
            self.aggiungi_button.state(["!disabled"])
        else:
            self.aggiungi_button.state(["disabled"])

    def iscrivi_atleta(self):
        input_window = tk.Toplevel(self.master)
        input_window.title("Iscrivi Atleta")

        cf_label = ttk.Label(input_window, text="Codice Fiscale:")
        cf_label.pack(side=tk.LEFT, padx=5, pady=5)
        cf_entry = ttk.Entry(input_window)
        cf_entry.pack(side=tk.LEFT, padx=5, pady=5)

        submit_button = ttk.Button(input_window, text="Conferma", command=lambda: self.submit_iscrizione(input_window, cf_entry))
        submit_button.pack(side=tk.LEFT, padx=5, pady=5)

        cf_entry.focus_set()

    def submit_iscrizione(self, input_window, cf_entry):
        partecipante_cf = cf_entry.get()
        if partecipante_cf:
            atleta = self.controller.get_atleta_by_cf(partecipante_cf)
            if atleta:
                success, message = self.controller.iscrivi_partecipante(self.gara, partecipante_cf)
                if success:
                    messagebox.showinfo("Successo", f"Atleta {atleta.nome} {atleta.cognome} iscritto con successo.")
                else:
                    messagebox.showerror("Errore", message)
                input_window.destroy()
                self.update_iscritti_list()
            else:
                messagebox.showerror("Errore", "Atleta non trovato.")
        else:
            messagebox.showerror("Errore", "Inserisci un codice fiscale valido.")

    def aggiungi_risultato(self):
        InserisciRisultatiView(tk.Toplevel(self.master), self.controller, self.gara)

    def update_iscritti_list(self):
        self.iscritti_listbox.delete(0, tk.END)
        partecipanti = self.gara.load_partecipanti()
        for cf in partecipanti:
            atleta = self.controller.get_atleta_by_cf(cf)
            if atleta:
                self.iscritti_listbox.insert(tk.END, f"{atleta.nome} {atleta.cognome} ({cf})")

    def update_risultati_list(self):
        self.risultati_listbox.delete(0, tk.END)
        risultati = self.gara.load_risultati()
        for cf, risultato in risultati.items():
            atleta = self.controller.get_atleta_by_cf(cf)
            if atleta:
                self.risultati_listbox.insert(tk.END, f"{atleta.nome} {atleta.cognome}: {risultato}")
