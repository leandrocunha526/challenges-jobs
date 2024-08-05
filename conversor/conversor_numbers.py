import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from conversor import Conversor

class ConversorNumeros:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Números")

        self.conversor = Conversor()

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

    def convert(self):
        if self.conversion_type.get() == 'Inteiro para Romano':
            try:
                num = int(self.entry.get())
                result = self.conversor.inteiro_para_romano(num)
                self.result_label.config(text=f'Número Romano: {result}')
            except ValueError:
                messagebox.showerror('Erro', 'Por favor, insira um número inteiro válido.')
        elif self.conversion_type.get() == 'Romano para Inteiro':
            roman_num = self.entry.get().strip()
            if not roman_num:
                messagebox.showerror('Erro', 'Por favor, insira um número romano válido.')
            else:
                try:
                    result = self.conversor.romano_para_inteiro(roman_num)
                    self.result_label.config(text=f'Número Inteiro: {result}')
                except KeyError:
                    messagebox.showerror('Erro', 'Número romano inválido.')

if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorNumeros(root)
    root.mainloop()
