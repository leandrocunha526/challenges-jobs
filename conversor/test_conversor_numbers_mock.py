import unittest
from unittest.mock import patch
import tkinter as tk
from conversor_numbers import ConversorNumeros
from conversor import Conversor


class TestConversorNumbers(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = ConversorNumeros(self.root)

    def tearDown(self):
        self.root.destroy()

    @patch.object(Conversor, 'inteiro_para_romano')
    def test_convert_inteiro_para_romano(self, mock_inteiro_para_romano):
        mock_inteiro_para_romano.return_value = 'X'
        self.app.conversion_type.set('Inteiro para Romano')
        self.app.entry.insert(0, '10')
        self.app.convert()
        self.assertEqual(self.app.result_label['text'], 'Número Romano: X')

    @patch.object(Conversor, 'romano_para_inteiro')
    def test_convert_romano_para_inteiro(self, mock_romano_para_inteiro):
        mock_romano_para_inteiro.return_value = 10
        self.app.conversion_type.set('Romano para Inteiro')
        self.app.entry.insert(0, 'X')
        self.app.convert()
        self.assertEqual(self.app.result_label['text'], 'Número Inteiro: 10')

if __name__ == "__main__":
    unittest.main()
