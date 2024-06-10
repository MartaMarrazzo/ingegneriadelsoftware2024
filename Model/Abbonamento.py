class Abbonamento:
    def __init__(self, nome, frequenza, importo_pagamento):
        self.nome = nome
        self.frequenza = frequenza
        self.importo_pagamento = importo_pagamento

    def get_abbonamenti():
        abbonamenti = [
            Abbonamento("Mensile", "1 mese", 60),
            Abbonamento("Trimestrale", "3 mesi", 150),
            Abbonamento("Semestrale", "6 mesi", 300),
            Abbonamento("Annuale", "12 mesi", 500),
            Abbonamento("Mensile Kids", "1 mese", 50),
            Abbonamento("Trimestrale Kids", "3 mesi", 135),
            Abbonamento("Semestrale Kids", "6 mesi", 250),
            Abbonamento("Annuale Kids", "12 mesi", 480)
        ]
        return abbonamenti
