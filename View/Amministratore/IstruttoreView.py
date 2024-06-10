
import tkinter as tk
from tkinter import ttk, messagebox


from Model.Istruttore import Istruttore


class IstruttoreView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Gestione Istruttori")

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Button to open the add instructor form
        ttk.Button(self.frame, text="Aggiungi Istruttore", command=self.open_add_istruttore_form).pack(side=tk.TOP,
                                                                                                       padx=10, pady=10)

        search_frame = ttk.LabelFrame(self.frame, text="Cerca Istruttore per Codice Fiscale", padding="10")
        search_frame.pack(fill=tk.X, expand=False, padx=10, pady=10)

        self.cf_search_entry = ttk.Entry(search_frame, width=30)
        self.cf_search_entry.pack(side=tk.LEFT, padx=5, pady=5)
        ttk.Button(search_frame, text="Cerca", command=self.fetch_and_display_istruttore).pack(side=tk.LEFT, padx=10,
                                                                                               pady=5)

        self.list_frame = ttk.LabelFrame(self.frame, text="Elenco Istruttori", padding="10")
        self.list_frame.pack(fill=tk.X, expand=False, padx=10, pady=10)

        self.elenco_istruttori_listbox = tk.Listbox(self.list_frame, height=6)
        self.elenco_istruttori_listbox.pack(padx=5, pady=5, fill=tk.X, expand=True)

        elenco_istruttori = Istruttore.get_lista_istruttori()

        for istruttore_key in elenco_istruttori:
            istruttore = elenco_istruttori[istruttore_key]
            if hasattr(istruttore, 'cf'):
                self.elenco_istruttori_listbox.insert(tk.END,
                                                      f" {istruttore.nome} {istruttore.cognome} - {istruttore.data_nascita}, {istruttore.cf}")
            else:
                print(f"Istruttore object is missing 'cf' attribute: {istruttore}")

    def open_add_istruttore_form(self):
        top = tk.Toplevel(self.master)
        top.title("Aggiungi istruttore")

        form_frame = ttk.LabelFrame(top, text="Informazioni istruttore", padding="10")
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        labels = ["Nome", "Cognome", "Data di nascita (YYYY-MM-DD)", "Luogo di nascita", "Codice fiscale", "Telefono",
                  "Livello dell'istruttore"]
        entries = {}
        livello_options = ["Viola", "Blu", "Marrone", "Nera"]

        for i, label in enumerate(labels):
            ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            if label == "Livello dell'istruttore":
                combo_livello = ttk.Combobox(form_frame, values=livello_options, width=27)
                combo_livello.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = combo_livello
            else:
                entry = ttk.Entry(form_frame, width=30)
                entry.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = entry

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=len(labels), column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Button(button_frame, text="Salva istruttore", command=lambda: self.add_istruttore(entries, top)).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=5,
                                                                                                                  pady=5)
        ttk.Button(button_frame, text="Annulla", command=top.destroy).grid(row=0, column=1, padx=5, pady=5)

    def add_istruttore(self, entries, window):
        istruttore_data = {
            'nome': entries['Nome'].get(),
            'cognome': entries['Cognome'].get(),
            'data_nascita': entries['Data di nascita (YYYY-MM-DD)'].get(),
            'luogo_nascita': entries['Luogo di nascita'].get(),
            'cf': entries['Codice fiscale'].get(),
            'telefono': entries['Telefono'].get(),
            'livello': entries['Livello dell\'istruttore'].get(),
        }
        success, message = self.controller.add_istruttore(istruttore_data)
        if success:
            messagebox.showinfo("Successo", message)
            window.destroy()  # Close the window if successful
        else:
            messagebox.showerror("Errore", message)

    def fetch_and_display_istruttore(self):
        cf = self.cf_search_entry.get()
        istruttore_data = self.controller.get_istruttore_by_cf(cf)
        if istruttore_data:
            self.open_elimina_istruttore_form(istruttore_data)
        else:
            messagebox.showerror("Errore", "Istruttore non trovato.")

    def open_elimina_istruttore_form(self, istruttore):
        top = tk.Toplevel(self.master)
        top.title("Elimina Istruttore")

        form_frame = ttk.LabelFrame(top, text="Conferma Eliminazione", padding="10")
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(form_frame,
                  text=f"Sei sicuro di voler eliminare l'istruttore: {istruttore.nome} {istruttore.cognome}?").grid(
            row=0, column=0, sticky="w")

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=1, column=0, pady=10, sticky="ew")

        ttk.Button(button_frame, text="Conferma", command=lambda: self.remove_istruttore(istruttore, top)).grid(row=0,
                                                                                                                column=0,
                                                                                                                padx=5,
                                                                                                                pady=5)
        ttk.Button(button_frame, text="Annulla", command=top.destroy).grid(row=0, column=1, padx=5, pady=5)

    def remove_istruttore(self, istruttore, top):
        success, message = self.controller.remove_istruttore(istruttore)
        if success:
            messagebox.showinfo("Successo", message)
            top.destroy()  # Chiude la finestra di conferma
            self.master.destroy()  # Chiude la finestra principale dopo la rimozione
        else:
            messagebox.showerror("Errore", message)