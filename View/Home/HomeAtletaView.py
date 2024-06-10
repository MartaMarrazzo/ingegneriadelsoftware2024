import tkinter as tk
from tkinter import ttk

from View.Atleta.BookingsView import BookingsView
from View.Atleta.GaraCalendarView import GaraCalendarView
from View.Atleta.PricesView import PricesView
from View.Atleta.TrainingCalendarView import TrainingCalendarView


class HomeAtletaView:
    def __init__(self, master, gara_controller, corso_controller, abbonamento_controller, user_cf):
        self.master = master
        self.master.geometry("400x400")
        self.master.title("Home Atleta")
        self.gara_controller = gara_controller
        self.corso_controller = corso_controller
        self.abbonamento_controller = abbonamento_controller
        self.user_cf = user_cf  # Memorizza il CF dell'utente corrente

        self.create_widgets()

    def create_widgets(self):
        athlete_frame = ttk.LabelFrame(self.master, text="Athlete", padding=(20, 10))
        athlete_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Button(athlete_frame, text="Prezzi", command=self.view_prices).grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        ttk.Button(athlete_frame, text="Calendario Gare", command=self.view_calendar).grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        ttk.Button(athlete_frame, text="Calendario Allenamenti", command=self.view_training_calendar).grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        ttk.Button(athlete_frame, text="Prenotazioni Gare", command=self.view_bookings).grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    def view_prices(self):
        PricesView(self.master, self.abbonamento_controller)

    def view_calendar(self):
        GaraCalendarView(self.master, self.gara_controller, self.user_cf)

    def view_training_calendar(self):
        TrainingCalendarView(self.master, self.corso_controller)

    def view_bookings(self):
        BookingsView(self.master, self.gara_controller, self.user_cf)


    """    
    def view_calendar(self):
        self.open_gara_calendar()

    def view_training_calendar(self):
        self.open_training_calendar()

    def view_bookings(self):
        self.open_bookings_view()
        
    def open_new_window(self, title, message):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)
        new_window.geometry("300x200")
        ttk.Label(new_window, text=message, padding=20).pack(expand=True)

    def open_gara_calendar(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Calendario Gare")
        new_window.geometry("800x400")  # Increased width to accommodate the booking button

        frame = ttk.Frame(new_window)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        tree = ttk.Treeview(frame, columns=("Nome", "Data", "Luogo", "Requisiti"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Data", text="Data")
        tree.heading("Luogo", text="Luogo")
        tree.heading("Requisiti", text="Requisiti")

        gare = self.gara_controller.get_gare()
        for gara in gare:
            tree.insert("", "end", values=(gara.nome, gara.data.strftime("%Y-%m-%d"), gara.luogo, gara.requisiti))

        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Booking Button
        ttk.Button(frame, text="Prenotati", command=lambda: self.book_gara(tree)).grid(row=1, column=0, pady=10, sticky="ew")

    def open_training_calendar(self):
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

    def get_current_user_cf(self):
        return self.user_cf

    def book_gara(self, tree):
        selected_item = tree.selection()
        if selected_item:
            gara_data = tree.item(selected_item[0], "values")
            gara_nome = gara_data[0]

            success, message = self.gara_controller.book_gara(gara_nome, self.get_current_user_cf())
            if success:
                self.open_new_window("Prenotazione Confermata", message)
            else:
                self.open_new_window("Errore", message)
        else:
            self.open_new_window("Errore", "Seleziona una gara per prenotarti.")

    def open_bookings_view(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Prenotazioni Gare")
        new_window.geometry("800x400")

        frame = ttk.Frame(new_window)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        tree = ttk.Treeview(frame, columns=("Nome", "Data", "Luogo", "Requisiti"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Data", text="Data")
        tree.heading("Luogo", text="Luogo")
        tree.heading("Requisiti", text="Requisiti")

        prenotazioni = self.gara_controller.get_prenotazioni(self.get_current_user_cf())
        for prenotazione in prenotazioni:
            tree.insert("", "end", values=(
            prenotazione.nome, prenotazione.data.strftime("%Y-%m-%d"), prenotazione.luogo, prenotazione.requisiti))

        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Delete Booking Button
        ttk.Button(frame, text="Cancella Prenotazione", command=lambda: self.delete_booking(tree)).grid(row=1, column=0,
                                                                                                        pady=10,
                                                                                                        sticky="ew")

    def delete_booking(self, tree):
        selected_item = tree.selection()
        if selected_item:
            booking_data = tree.item(selected_item[0], "values")
            gara_nome = booking_data[0]

            success, message = self.gara_controller.delete_prenotazione(gara_nome, self.get_current_user_cf())
            if success:
                tree.delete(selected_item)
                self.open_new_window("Prenotazione Cancellata", message)
            else:
                self.open_new_window("Errore", message)
        else:
            self.open_new_window("Errore", "Seleziona una prenotazione da cancellare.")

    def view_prices(self):
        self.abbonamento_controller.view_prices()

    def open_prices_window(self, abbonamenti):
        new_window = tk.Toplevel(self.master)
        new_window.title("Prezzi Abbonamenti")
        new_window.geometry("600x300")

        frame = ttk.Frame(new_window)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        tree = ttk.Treeview(frame, columns=("Nome", "Frequenza", "Prezzo"), show='headings')
        tree.heading("Nome", text="Nome")
        tree.heading("Frequenza", text="Frequenza")
        tree.heading("Prezzo", text="Prezzo")

        for abbonamento in abbonamenti:
            tree.insert("", "end", values=(abbonamento.nome, abbonamento.frequenza, abbonamento.importo_pagamento))

        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")
"""
