import tkinter as tk
from tkinter import ttk, messagebox

class InserisciRisultatiView:
    def __init__(self, master, controller, gara):
        self.master = master
        self.controller = controller
        self.gara = gara
        self.master.title("Inserisci Risultati Gare")

        self.setup_gui()

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.frame, text="Partecipante").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(self.frame, text="Risultato").grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.result_entries = {}
        partecipanti = self.gara.load_partecipanti()
        result_options = ["oro", "argento", "bronzo", "no-podio", "squalifica"]

        # Initialize i to ensure it's defined
        i = 0
        for i, cf in enumerate(partecipanti, start=1):
            atleta = self.controller.get_atleta_by_cf(cf)
            if atleta:
                ttk.Label(self.frame, text=f"{atleta.nome} {atleta.cognome}").grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
                result_entry = ttk.Combobox(self.frame, values=result_options, width=30)
                result_entry.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                self.result_entries[cf] = result_entry

        # Ensure the button is placed correctly even if no participants
        ttk.Button(self.frame, text="Registra Risultati", command=self.save_all_results).grid(row=i + 1, column=0, columnspan=2, pady=10)

    def save_all_results(self):
        for cf, combobox in self.result_entries.items():
            risultato = combobox.get()
            if risultato:  # Ensure there is a result before saving
                success, message = self.controller.save_result(self.gara, cf, risultato)
                if not success:
                    messagebox.showerror("Errore", f"Errore per {cf}: {message}")
                    return

        messagebox.showinfo("Successo", "Tutti i risultati sono stati registrati con successo!")
        self.master.destroy()

