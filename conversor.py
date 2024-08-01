import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ConversorNumeros:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Números")

        # Tipo de conversão
        self.conversion_type = ttk.Combobox(root, values=['Inteiro para Romano', 'Romano para Inteiro'])
        self.conversion_type.grid(column=0, row=0, padx=10, pady=10)
        self.conversion_type.current(0)

        # Campo de entrada
        self.entry = ttk.Entry(root, width=20)
        self.entry.grid(column=1, row=0, padx=10, pady=10)

        # Botão para converter
        self.convert_button = ttk.Button(root, text="Converter", command=self.convert)
        self.convert_button.grid(column=2, row=0, padx=10, pady=10)

        # Label para mostrar o resultado
        self.result_label = ttk.Label(root, text="Resultado")
        self.result_label.grid(column=0, row=1, columnspan=3, pady=10)

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

    def convert(self):
        if self.conversion_type.get() == 'Inteiro para Romano':
            try:
                num = int(self.entry.get())
                result = self.inteiro_para_romano(num)
                self.result_label.config(text=f'Número Romano: {result}')
            except ValueError:
                messagebox.showerror('Erro', 'Por favor, insira um número inteiro válido.')
        elif self.conversion_type.get() == 'Romano para Inteiro':
            roman_num = self.entry.get().strip()
            if not roman_num:
                messagebox.showerror('Erro', 'Por favor, insira um número romano válido.')
            else:
                try:
                    result = self.romano_para_inteiro(roman_num)
                    self.result_label.config(text=f'Número Inteiro: {result}')
                except KeyError:
                    messagebox.showerror('Erro', 'Número romano inválido.')

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorNumeros(root)
    root.mainloop()
