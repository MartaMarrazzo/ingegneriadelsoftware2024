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
