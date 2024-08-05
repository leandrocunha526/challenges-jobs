class Conversor:
    def inteiro_para_romano(self, num):
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
