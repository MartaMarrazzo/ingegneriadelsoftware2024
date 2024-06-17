from View.Amministratore.GestioneGaraView import GestioneGaraView


class InserisciGaraView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Registrazione Gara")
        self.setup_gui()

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        labels = ["Nome Gara", "Data Gara (YYYY-MM-DD)", "Luogo Gara", "Requisiti Gara"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            entry = ttk.Entry(self.frame, width=30)
            entry.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
            self.entries[label] = entry

        ttk.Button(self.frame, text="Registra Gara", command=self.registra_gara).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def registra_gara(self):
        nome = self.entries["Nome Gara"].get().strip()
        data = self.entries["Data Gara (YYYY-MM-DD)"].get().strip()
        luogo = self.entries["Luogo Gara"].get().strip()
        requisiti = self.entries["Requisiti Gara"].get().strip()

        if nome and data and luogo:
            gara = self.controller.crea_gara(nome, data, luogo, requisiti)
            messagebox.showinfo("Successo", f"Gara registrata con successo!")
            self.master.destroy()
        else:
            messagebox.showerror("Errore", "Tutti i campi sono obbligatori.")

class CercaGaraView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Cerca Gara")
        self.setup_gui()

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        search_frame = ttk.LabelFrame(self.frame, text="Cerca Gara per Nome", padding="10")
        search_frame.pack(fill=tk.X, expand=False, padx=10, pady=10)

        self.nome_entry = ttk.Entry(search_frame, width=30)
        self.nome_entry.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Button(search_frame, text="Cerca", command=self.cerca_gara).pack(side=tk.LEFT, padx=10, pady=5)

    def cerca_gara(self):
        nome = self.nome_entry.get()
        if nome:
            gara = self.controller.get_gara_by_nome(nome)
            if gara:
                # Apri una finestra di gestione per la gara trovata
                new_window = tk.Toplevel(self.master)
                GestioneGaraView(new_window, self.controller, gara)
                messagebox.showinfo("Risultato Ricerca", f"Gara trovata: {gara.nome} - {gara.data} - {gara.luogo}")
            else:
                messagebox.showerror("Errore", "Gara non trovata.")
        else:
            messagebox.showerror("Errore", "Inserire il nome della gara da cercare.")
import tkinter as tk
from tkinter import ttk, messagebox

class GestioneGareView:
    def __init__(self, master, controller, atletla_controller):
        self.master = master
        self.controller = controller
        self.atleta_controller = atletla_controller
        self.master.title("Gestione Gare")

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Button(self.frame, text="Inserisci Gara", command=self.inserisci_gara).pack(pady=5)
        ttk.Button(self.frame, text="Cerca Gara", command=self.cerca_gara).pack(pady=5)

        self.gare_listbox = tk.Listbox(self.frame)
        self.gare_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.update_gare_list()

    def update_gare_list(self):
        self.gare_listbox.delete(0, tk.END)
        for gara in self.controller.get_gare():
            self.gare_listbox.insert(tk.END, f"{gara.nome} - {gara.data} - {gara.luogo}")

    def inserisci_gara(self):
        new_window = tk.Toplevel(self.master)
        InserisciGaraView(new_window, self.controller)

    def cerca_gara(self):
        new_window = tk.Toplevel(self.master)
        CercaGaraView(new_window, self.controller)
