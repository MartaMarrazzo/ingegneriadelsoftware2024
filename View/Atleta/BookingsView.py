import tkinter as tk
from tkinter import ttk, messagebox


class BookingsView:
    def __init__(self, master, gara_controller, user_cf):
        self.master = master
        self.gara_controller = gara_controller
        self.user_cf = user_cf

        self.create_widgets()

    def create_widgets(self):
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

        prenotazioni = self.gara_controller.get_prenotazioni(self.user_cf)
        for prenotazione in prenotazioni:
            tree.insert("", "end", values=(prenotazione.nome, prenotazione.data.strftime("%Y-%m-%d"), prenotazione.luogo, prenotazione.requisiti))

        tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Delete Booking Button
        ttk.Button(frame, text="Cancella Prenotazione", command=lambda: self.delete_booking(tree)).grid(row=1, column=0, pady=10, sticky="ew")

    def delete_booking(self, tree):
        selected_item = tree.selection()
        if selected_item:
            booking_data = tree.item(selected_item[0], "values")
            gara_nome = booking_data[0]
            # Richiesta di conferma
            confirm = messagebox.askyesno("Conferma Eliminazione",
                                          f"Sei sicuro di voler eliminare la prenotazione per la gara: {gara_nome}?")
            if confirm:
                success, message = self.gara_controller.delete_prenotazione(gara_nome, self.user_cf)
                if success:
                    tree.delete(selected_item)
                    self.open_new_window("Prenotazione Cancellata", message)
                else:
                    self.open_new_window("Errore", message)
        else:
            self.open_new_window("Errore", "Seleziona una prenotazione da cancellare.")

    def open_new_window(self, title, message):
        new_window = tk.Toplevel(self.master)
        new_window.title(title)
        new_window.geometry("300x200")
        ttk.Label(new_window, text=message, padding=20).pack(expand=True)
