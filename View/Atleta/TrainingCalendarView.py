import tkinter as tk
from tkinter import ttk

class TrainingCalendarView:
    def __init__(self, master, corso_controller):
        self.master = master
        self.corso_controller = corso_controller

        self.create_widgets()

    def create_widgets(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Calendario Allenamenti")
        new_window.geometry("600x400")

        allenamenti = self.corso_controller.get_all_allenamenti()
        giorni_settimana = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato"]

        tree = ttk.Treeview(new_window, columns=("Corso", "Ora Inizio", "Ora Fine", "Istruttore"), show='headings')
        tree.heading("Corso", text="Corso")
        tree.heading("Ora Inizio", text="Ora Inizio")
        tree.heading("Ora Fine", text="Ora Fine")
        tree.heading("Istruttore", text="Istruttore")

        for giorno in giorni_settimana:
            tree.insert("", "end", values=(f"-------- {giorno} --------", "", "", ""))
            for allenamento in allenamenti:
                if allenamento.giorno == giorno:
                    tree.insert("", "end", values=(allenamento.corso, allenamento.ora_inizio, allenamento.ora_fine, allenamento.istruttore))

        tree.pack(expand=True, fill='both')
