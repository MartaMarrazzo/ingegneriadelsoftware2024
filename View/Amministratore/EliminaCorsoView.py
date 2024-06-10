from tkinter import ttk

import tk


class EliminaCorsoView(tk.Toplevel):
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.title("Elimina Corso")

        self.frame = ttk.Frame(self)
        self.frame.pack(padx=10, pady=10)

        self.nome_label = ttk.Label(self.frame, text="Nome Corso:")
        self.nome_label.grid(row=0, column=0, sticky="w")
        self.nome_entry = ttk.Entry(self.frame)
        self.nome_entry.grid(row=0, column=1)

        self.elimina_button = ttk.Button(self.frame, text="Elimina", command=self.elimina_corso)
        self.elimina_button.grid(row=1, columnspan=2, pady=5)

    def elimina_corso(self):
        nome = self.nome_entry.get()
