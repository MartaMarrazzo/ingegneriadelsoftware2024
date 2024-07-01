import tkinter as tk
from tkinter import ttk
from Controller.StatisticheController import StatisticheController


class StatisticheView:
    def __init__(self, root):
        self.root = root
        self.root.title("Statistiche e Dati")

        # Configurazione della finestra principale
        self.frame = ttk.Frame(self.root, padding="10")
        self.frame.grid(row=0, column=0)

        # Titolo
        self.title_label = ttk.Label(self.frame, text="Statistiche Gare per Livello Atleti", font=("Helvetica", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Area di testo per visualizzare le statistiche
        self.text_area = tk.Text(self.frame, width=80, height=20, wrap="word", state='disabled')
        self.text_area.grid(row=1, column=0, columnspan=2, pady=10)

        # Bottone per caricare le statistiche
        self.load_button = ttk.Button(self.frame, text="Carica Statistiche", command=self.visualizza_statistiche)
        self.load_button.grid(row=2, column=0, columnspan=2, pady=10)

    def mostra_statistiche_iscritti(self, totale_iscritti, iscritti_per_livello, percentuali_per_livello):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"Totale Iscritti: {totale_iscritti}\n\n")
        self.text_area.insert(tk.END, "Iscritti per Livello:\n")
        for livello, count in iscritti_per_livello.items():
            self.text_area.insert(tk.END, f"  Livello {livello}: {count} ({percentuali_per_livello[livello]:.2f}%)\n")
        self.text_area.insert(tk.END, "\n")
        self.text_area.config(state='disabled')

    def mostra_statistiche_risultati(self, totale_risultati, risultati_per_livello, percentuali_risultati):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"Totale Risultati: {totale_risultati}\n\n")
        self.text_area.insert(tk.END, "Risultati per Livello:\n")
        for livello, count in risultati_per_livello.items():
            self.text_area.insert(tk.END, f"  Livello {livello}: {count} ({percentuali_risultati[livello]:.2f}%)\n")
        self.text_area.insert(tk.END, "\n")
        self.text_area.config(state='disabled')

    def mostra_certificati_in_scadenza(self, certificati_settimana, certificati_mese):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, "Certificati Medici in Scadenza nella Prossima Settimana:\n")
        for atleta in certificati_settimana:
            self.text_area.insert(tk.END,
                                  f"  {atleta.nome} {atleta.cognome} - Scadenza: {atleta.scadenza_certificato_medico.date()}\n")
        self.text_area.insert(tk.END, "\n")

        self.text_area.insert(tk.END, "Certificati Medici in Scadenza nel Prossimo Mese:\n")
        for atleta in certificati_mese:
            self.text_area.insert(tk.END,
                                  f"  {atleta.nome} {atleta.cognome} - Scadenza: {atleta.scadenza_certificato_medico.date()}\n")
        self.text_area.insert(tk.END, "\n")
        self.text_area.config(state='disabled')

    def mostra_statistiche_risultati_tipo(self, totale_risultati, tipi_risultati, percentuali_risultati):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"Totale Risultati: {totale_risultati}\n\n")
        self.text_area.insert(tk.END, "Risultati per Tipo:\n")
        for tipo, count in tipi_risultati.items():
            self.text_area.insert(tk.END, f"  {tipo.capitalize()}: {count} ({percentuali_risultati[tipo]:.2f}%)\n")
        self.text_area.insert(tk.END, "\n")
        self.text_area.config(state='disabled')

    def visualizza_statistiche(self):
        self.text_area.config(state='normal')
        self.text_area.delete("1.0", tk.END)  # Clear the text area before inserting new data
        self.text_area.config(state='disabled')

        certificati_settimana, certificati_mese = StatisticheController.get_certificati_in_scadenza()
        self.mostra_certificati_in_scadenza(certificati_settimana, certificati_mese)

        totale_iscritti, iscritti_per_livello, percentuali_per_livello = StatisticheController.get_statistiche_iscritti_per_livello()
        self.mostra_statistiche_iscritti(totale_iscritti, iscritti_per_livello, percentuali_per_livello)

        totale_risultati, risultati_per_livello, percentuali_risultati = StatisticheController.get_statistiche_risultati_per_livello()
        self.mostra_statistiche_risultati(totale_risultati, risultati_per_livello, percentuali_risultati)

        totale_risultati, tipi_risultati, percentuali_risultati = StatisticheController.get_statistiche_risultati_tipo()
        self.mostra_statistiche_risultati_tipo(totale_risultati, tipi_risultati, percentuali_risultati)

