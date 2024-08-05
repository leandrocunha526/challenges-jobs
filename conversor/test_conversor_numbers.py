import unittest
from conversor import Conversor


class TestConversor(unittest.TestCase):

    def setUp(self):
        self.conversor = Conversor()

    def test_inteiro_para_romano(self):
        self.assertEqual(self.conversor.inteiro_para_romano(1), 'I')
        self.assertEqual(self.conversor.inteiro_para_romano(4), 'IV')
        self.assertEqual(self.conversor.inteiro_para_romano(9), 'IX')
        self.assertEqual(self.conversor.inteiro_para_romano(58), 'LVIII')
        self.assertEqual(self.conversor.inteiro_para_romano(1994), 'MCMXCIV')

    def test_romano_para_inteiro(self):
        self.assertEqual(self.conversor.romano_para_inteiro('I'), 1)
        self.assertEqual(self.conversor.romano_para_inteiro('IV'), 4)
        self.assertEqual(self.conversor.romano_para_inteiro('IX'), 9)
        self.assertEqual(self.conversor.romano_para_inteiro('LVIII'), 58)
        self.assertEqual(self.conversor.romano_para_inteiro('MCMXCIV'), 1994)

if __name__ == "__main__":
    unittest.main()
