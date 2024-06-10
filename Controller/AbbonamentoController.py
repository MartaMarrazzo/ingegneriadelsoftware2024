class AbbonamentoController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def view_prices(self):
        return self.model.get_abbonamenti()
