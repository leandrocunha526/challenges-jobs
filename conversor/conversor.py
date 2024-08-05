"""
Módulo para conversão de números inteiros para números romanos e vice-versa.

Este módulo contém a classe Conversor que fornece dois métodos:
- inteiro_para_romano: Converte um número inteiro em um número romano.
- romano_para_inteiro: Converte um número romano em um número inteiro.
Módulo em conformidade com PEP 257.
"""

class Conversor:
    """Classe para conversão de números inteiros e números romanos."""

    def inteiro_para_romano(self, num):
        """
        Converte um número inteiro em um número romano.

        Args:
            num (int): O número inteiro a ser convertido.

        Returns:
            str: A representação do número romano.
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def romano_para_inteiro(self, roman):
        """
        Converte um número romano em um número inteiro.

        Args:
            roman (str): O número romano a ser convertido.

        Returns:
            int: A representação do número inteiro.
        """
        roman = roman.upper()
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        inteiro = 0
        prev_value = 0
        for char in roman:
            value = roman_dict.get(char, 0)
            if value > prev_value:
                inteiro += value - 2 * prev_value
            else:
                inteiro += value
            prev_value = value
        return inteiro
