import tkinter as tk
from tkinter import ttk, messagebox

from Controller.AbbonamentoController import AbbonamentoController
from Model.Atleta import Atleta


class DettagliAtletaView(tk.Toplevel):
    def __init__(self, parent, atleta):
        super().__init__(parent)
        self.title("Dettagli Atleta")

        self.atleta = atleta

        self.dettagli_frame = ttk.Frame(self)
        self.dettagli_frame.pack(padx=10, pady=10)

        ttk.Label(self.dettagli_frame, text=f"Atleta: {atleta.nome} {atleta.cognome}").grid(row=0, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Codice Fiscale: {atleta.cf} ").grid(row=1, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Luogo e Data di nascita: {atleta.luogo_nascita}, {atleta.data_nascita}").grid(row=3, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Telefono: {atleta.telefono} ").grid(row=4, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Livello: {atleta.livello_atleta} ").grid(row=5, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Abbonamento Sottoscritto: {atleta.tipo_abbonamento} ").grid(row=6, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Pagamento Assicurazione: {atleta.pagamento_assicurazione} ").grid(row=7, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Data Scadenza Certificato Medico: {atleta.scadenza_certificato_medico} ").grid(row=8, column=0, sticky="w")
        ttk.Label(self.dettagli_frame, text=f"Codice Fiscale Genitore - presente se atleta minorenne: {atleta.cf_genitore} ").grid(row=9, column=0, sticky="w")

class AtletaView:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller
        self.master.title("Gestione Atleti")

    def show_message(self, message):
        messagebox.showinfo("Info", message)

    def setup_gui(self):
        self.frame = ttk.Frame(self.master)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Button to open the add athlete form
        ttk.Button(self.frame, text="Aggiungi Atleta", command=self.open_add_atleta_form,).pack(side=tk.TOP, padx=10, pady=10)

        search_frame = ttk.LabelFrame(self.frame, text="Cerca Atleta per Codice Fiscale", padding="10")
        search_frame.pack(fill=tk.X, expand=False, padx=10, pady=10)

        self.cf_search_entry = ttk.Entry(search_frame, width=30)
        self.cf_search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        ttk.Button(search_frame, text="Cerca", command=self.fetch_and_display_atleta).pack(side=tk.LEFT, padx=10,
                                                                                           pady=5)

        self.list_frame = ttk.LabelFrame(self.frame, text="Elenco Atleti", padding="10")
        self.list_frame.pack(fill=tk.X, expand=False, padx=10, pady=10)

        self.elenco_atleti_listbox = tk.Listbox(self.list_frame, height=6)
        self.elenco_atleti_listbox.pack(padx=5, pady=5, fill=tk.X, expand=True)

        elenco_atleti = Atleta.get_lista_atleti()
        # Now iterating over the values of the dictionary, which are Atleta objects
        for atleta_key in elenco_atleti:
            atleta = elenco_atleti[atleta_key]
            self.elenco_atleti_listbox.insert(tk.END,
                                              f" {atleta.cf} : {atleta.nome} {atleta.cognome} - {atleta.data_nascita}, {atleta.luogo_nascita}")
            self.elenco_atleti_listbox.bind("<Double-Button-1>", self.mostra_dettagli_atleta)

        self.update_atleti_listbox()
    def open_add_atleta_form(self):
        top = tk.Toplevel(self.master)
        top.title("Aggiungi Atleta")

        form_frame = ttk.LabelFrame(top, text="Informazioni Atleta", padding="10")
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        labels = ["Nome", "Cognome", "Data di nascita (YYYY-MM-DD)", "Luogo di nascita", "Codice fiscale", "Telefono",
                  "Livello dell'atleta", "Tipo di abbonamento", "Codice fiscale del genitore",
                  "Pagamento assicurazione", "Scadenza certificato medico (YYYY-MM-DD)"]
        entries = {}
        livello_options = ["Bianca","Verde","Arancio","Viola", "Blu", "Marrone", "Nera"]

        abbonamenti = self.controller.abbonamento_controller.view_prices()
        abbonamento_options = [abbonamento.nome for abbonamento in abbonamenti]

        assicurazione_options = ["SI","NO"]

        for i, label in enumerate(labels):
            ttk.Label(form_frame, text=label).grid(row=i, column=0, sticky=tk.W, padx=5, pady=5)
            if label == "Livello dell'atleta":
                combo_livello = ttk.Combobox(form_frame, values=livello_options, width=27)
                combo_livello.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = combo_livello
            elif label == "Tipo di abbonamento":
                combo_abbonamento = ttk.Combobox(form_frame, values=abbonamento_options, width=27)
                combo_abbonamento.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = combo_abbonamento
            elif label == "Tipo di abbonamento":
                combo_abbonamento = ttk.Combobox(form_frame, values=abbonamento_options, width=27)
                combo_abbonamento.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = combo_abbonamento
            else:
                entry = ttk.Entry(form_frame, width=30)
                entry.grid(row=i, column=1, sticky=tk.E, padx=5, pady=5)
                entries[label] = entry

        button_frame = ttk.Frame(form_frame)
        button_frame.grid(row=len(labels), column=0, columnspan=2, pady=10, sticky="ew")

        ttk.Button(button_frame, text="Salva Atleta", command=lambda: self.add_atleta(entries, top)).grid(row=0,
                                                                                                          column=0,
                                                                                                          padx=5,
                                                                                                          pady=5)

        ttk.Button(button_frame, text="Annulla", command=top.destroy).grid(row=0, column=1, padx=5, pady=5)

    def add_atleta(self, entries, window):
        atleta_data = {
            'nome': entries['Nome'].get(),
            'cognome': entries['Cognome'].get(),
            'data_nascita': entries['Data di nascita (YYYY-MM-DD)'].get(),
            'luogo_nascita': entries['Luogo di nascita'].get(),
            'cf': entries['Codice fiscale'].get(),
            'telefono': entries['Telefono'].get(),
            'livello_atleta': entries['Livello dell\'atleta'].get(),
            'tipo_abbonamento': entries['Tipo di abbonamento'].get(),
            'cf_genitore': entries['Codice fiscale del genitore'].get(),
            'pagamento_assicurazione': entries['Pagamento assicurazione'].get(),
            'scadenza_certificato_medico': entries['Scadenza certificato medico (YYYY-MM-DD)'].get()
        }
        success, message = self.controller.add_atleta(atleta_data)
        if success:
            messagebox.showinfo("Successo", message)
            window.destroy()  # Close the window if successful
            self.update_atleti_listbox()
        else:
            messagebox.showerror("Errore", message)

    def fetch_and_display_atleta(self):
        cf = self.cf_search_entry.get()
        atleta_data = self.controller.get_atleta_by_cf(cf)
        if atleta_data:
            self.open_modifica_atleta_form(atleta_data)
        else:
            messagebox.showerror("Errore", "view : Atleta non trovato.")

    def open_modifica_atleta_form(self, atleta):
        top = tk.Toplevel(self.master)
        top.title("Modifica Atleta")

        form_frame = ttk.LabelFrame(top, text="Dati Atleta", padding="10")
        form_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Labels and attribute names
        labels = ["Nome", "Cognome", "Data di nascita", "Luogo di nascita", "Codice fiscale", "Telefono",
                  "Livello dell'atleta", "Tipo di abbonamento", "Codice Fiscale Genitore - se presente",
                  "Pagamento assicurazione", "Scadenza certificato medico"]
        attributes = ["nome", "cognome", "data_nascita", "luogo_nascita", "cf", "telefono", "livello_atleta",
                      "tipo_abbonamento", "cf_genitore", "pagamento_assicurazione", "scadenza_certificato_medico"]

        atleta_data = self.controller.get_atleta_by_cf(atleta.cf)

        # Dictionary to hold the Entry widgets for editable fields
        entries = {}

        # Options for dropdown menus
        livello_options = ["Bianca", "Verde", "Arancio", "Viola", "Blu", "Marrone", "Nera"]
        abbonamenti = self.controller.abbonamento_controller.view_prices()
        abbonamento_options = [abbonamento.nome for abbonamento in abbonamenti]
        assicurazione_options = ["SI", "NO"]

        # Row counter
        row = 0
        # Iterate through labels and attributes
        for label, attr in zip(labels, attributes):
            # Get the attribute value from the Atleta object
            value = getattr(atleta, attr, "")

            # Create label for non-editable fields
            ttk.Label(form_frame, text=label).grid(row=row, column=0, sticky=tk.W, padx=5, pady=5)

            # If the attribute is one of the non-editable fields, display it as label
            if attr in ["nome", "cognome", "data_nascita", "luogo_nascita", "cf"]:
                ttk.Label(form_frame, text=value).grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
            else:  # Otherwise, display it as an editable Entry field
                if attr == "livello_atleta":
                    combo_livello = ttk.Combobox(form_frame, values=livello_options, width=27)
                    combo_livello.set(value)
                    combo_livello.grid(row=row, column=1, sticky=tk.E, padx=5, pady=5)
                    entries[attr] = combo_livello
                elif attr == "tipo_abbonamento":
                    combo_abbonamento = ttk.Combobox(form_frame, values=abbonamento_options, width=27)
                    combo_abbonamento.set(value)
                    combo_abbonamento.grid(row=row, column=1, sticky=tk.E, padx=5, pady=5)
                    entries[attr] = combo_abbonamento
                elif attr == "pagamento_assicurazione":
                    combo_assicurazione = ttk.Combobox(form_frame, values=assicurazione_options, width=27)
                    combo_assicurazione.set(value)
                    combo_assicurazione.grid(row=row, column=1, sticky=tk.E, padx=5, pady=5)
                    entries[attr] = combo_assicurazione
                else:
                    var = tk.StringVar(top, value=value)
                    entry = ttk.Entry(form_frame, textvariable=var)
                    entry.grid(row=row, column=1, sticky=tk.W, padx=5, pady=5)
                    entries[attr] = var
            # Increment row counter
            row += 1

        # Button to save changes
        ttk.Button(form_frame, text="Salva Modifiche", command=lambda: self.save_changes2(entries, atleta, top)).grid(
            row=row, column=0, columnspan=4, pady=10)
        # Button to delete athlete
        ttk.Button(form_frame, text="Elimina Atleta", command=lambda: self.remove_atleta(atleta, top)).grid(
            row=row, column=2, columnspan=4, pady=10)

    """def save_changes(self, entries, atleta, window):
        updated_data = {label: entry.get() for label, entry in entries.items()}
        success = self.controller.update_atleta2(atleta, updated_data, window)"""

    def remove_atleta(self, atleta, window):
        self.controller.remove_atleta(atleta, window)  # Chiama la funzione di rimozione senza aspettarsi un risultato
        window.destroy()  # Chiudi la finestra
        self.update_atleti_listbox()  # Aggiorna la lista degli atleti

    def save_changes2(self, entries, atleta, window):
        updated_data = {attr: var.get() for attr, var in entries.items()}
        success, message = self.controller.update_atleta2(atleta, updated_data, window)
        if success:
            messagebox.showinfo("Successo", message)
            window.destroy()  # Close the window after successful update
            self.update_atleti_listbox()
        else:
            messagebox.showerror("Errore", message)

    def mostra_dettagli_atleta(self, event):
        selection_index = self.elenco_atleti_listbox.curselection()
        if selection_index:
            index = selection_index[0]
            cf = self.elenco_atleti_listbox.get(index).split()[0]  # Assuming the CF is the first item
            atleta = self.controller.get_atleta_by_cf(cf)
            if atleta:
                dettagli_view = DettagliAtletaView(self.master, atleta)
                dettagli_view.grab_set()
                dettagli_view.focus_set()
                dettagli_view.wait_window()

    def update_atleti_listbox(self):
        self.elenco_atleti_listbox.delete(0, tk.END)
        elenco_atleti = Atleta.get_lista_atleti()
        for atleta_key in elenco_atleti:
            atleta = elenco_atleti[atleta_key]
            self.elenco_atleti_listbox.insert(tk.END,
                                              f"{atleta.cf} : {atleta.nome} {atleta.cognome} - {atleta.data_nascita}, {atleta.luogo_nascita}")
        self.elenco_atleti_listbox.bind("<Double-Button-1>", self.mostra_dettagli_atleta)
