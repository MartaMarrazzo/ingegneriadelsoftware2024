import tkinter as tk
from tkinter import ttk

class GaraCalendarView:
    def __init__(self, master, gara_controller, user_cf):
        self.master = master
        self.gara_controller = gara_controller
        self.user_cf = user_cf

        self.create_widgets()

    def create_widgets(self):
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

    def book_gara(self, tree):
        selected_item = tree.selection()
        if selected_item:
            gara_data = tree.item(selected_item[0], "values")
            gara_nome = gara_data[0]

            success, message = self.gara_controller.book_gara(gara_nome, self.user_cf)
            if success:
                self.open_new_window("Prenotazione Confermata", message)
            else:
                self.open_new_window("Errore", message)
        else:
            self.open_new_window("Errore", "Seleziona una gara per prenotarti.")

    def open_new_window(self, title, message):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)
        new_window.geometry("300x200")
        ttk.Label(new_window, text=message, padding=20).pack(expand=True)
