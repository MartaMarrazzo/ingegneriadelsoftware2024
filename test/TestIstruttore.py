import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
from Model.Istruttore import Istruttore
from Controller.IstruttoreController import IstruttoreController
from View.Amministratore.IstruttoreView import IstruttoreView


class TestIstruttore(unittest.TestCase):

    def setUp(self):
        # Setup for the Istruttore model
        self.istruttore_data = {
            'nome': 'Mario',
            'cognome': 'Rossi',
            'data_nascita': '1980-01-01',
            'luogo_nascita': 'Roma',
            'cf': 'RSSMRA80A01H501Z',
            'telefono': '1234567890',
            'livello': 'Nera'
        }
        self.istruttore = Istruttore(**self.istruttore_data)

    def test_is_valid(self):
        valid, message = self.istruttore.is_valid()
        self.assertTrue(valid)
        self.assertEqual(message, '')

    def test_is_not_valid_cf(self):
        self.istruttore.cf = 'INVALIDCF'
        valid, message = self.istruttore.is_valid()
        self.assertFalse(valid)
        self.assertEqual(message, 'Codice fiscale deve essere di 16 caratteri alfanumerici.')

    def test_is_not_valid_phone(self):
        self.istruttore.telefono = '12345'
        valid, message = self.istruttore.is_valid()
        self.assertFalse(valid)
        self.assertEqual(message, 'Numero di telefono deve essere di 10 cifre numeriche.')

class TestIstruttoreController(unittest.TestCase):

    def setUp(self):
        # Setup for the IstruttoreController
        self.model = MagicMock()
        self.view = MagicMock()
        self.controller = IstruttoreController(self.model, self.view)
        self.istruttore_data = {
            'nome': 'Mario',
            'cognome': 'Rossi',
            'data_nascita': '1980-01-01',
            'luogo_nascita': 'Roma',
            'cf': 'RSSMRA80A01H501Z',
            'telefono': '1234567890',
            'livello': 'Nera'
        }

    def test_add_istruttore_success(self):
        self.model.ricercaIstruttore.return_value = None
        new_istruttore = Istruttore(**self.istruttore_data)
        self.model.add_istruttore.return_value = True, "Istruttore aggiunto con successo."

        success, message = self.controller.add_istruttore(self.istruttore_data)
        self.assertTrue(success)
        self.assertEqual(message, "Istruttore aggiunto con successo.")

    def test_add_istruttore_existing(self):
        self.model.ricercaIstruttore.return_value = Istruttore(**self.istruttore_data)

        success, message = self.controller.add_istruttore(self.istruttore_data)
        self.assertFalse(success)
        self.assertEqual(message, "Un istruttore con questo codice fiscale esiste già.")

class TestIstruttoreView(unittest.TestCase):

    def setUp(self):
        # Setup for the IstruttoreView
        self.root = tk.Tk()
        self.controller = MagicMock()
        self.view = IstruttoreView(self.root, self.controller)

    def tearDown(self):
        self.root.destroy()

    def test_show_message(self):
        with patch('tkinter.messagebox.showinfo') as mock_showinfo:
            self.view.show_message("Test Message")
            mock_showinfo.assert_called_with("Info", "Test Message")

    def test_open_add_istruttore_form(self):
        with patch.object(self.view, 'add_istruttore', return_value=None):
            self.view.open_add_istruttore_form()
            self.assertIsInstance(self.view.master.children['!toplevel'], tk.Toplevel)

if __name__ == '__main__':
    unittest.main()
