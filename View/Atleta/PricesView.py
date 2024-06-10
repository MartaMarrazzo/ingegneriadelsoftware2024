import tkinter as tk
from tkinter import ttk

class PricesView:
    def __init__(self, master, abbonamento_controller):
        self.master = master
        self.abbonamento_controller = abbonamento_controller

        self.create_widgets()

    def create_widgets(self):
        abbonamenti = self.abbonamento_controller.view_prices()
        self.open_prices_window(abbonamenti)

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
