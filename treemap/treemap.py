import tkinter as tk
from tkinter import ttk
import requests
import plotly.express as px
import pandas as pd


class CryptoAnalyzer:

    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("Análise de Criptomoedas")
        self.root.geometry("500x300")

        # Criação do frame principal
        self.mainframe = ttk.Frame(root, padding="10 10 10 10")
        self.mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # Criação dos widgets da interface
        self.create_widgets()

    def create_widgets(self):
        """Cria os widgets da interface gráfica."""
        # Botão para mostrar o Tree Map
        ttk.Button(
            self.mainframe,
            text="Mostrar TreeMap",
            command=self.on_show_treemap
        ).grid(column=1, row=1, sticky=tk.W)

        # Descrição do botão
        ttk.Label(
            self.mainframe,
            text="Clique no botão para exibir um TreeMap com a capitalização de mercado e a variação percentual das criptomoedas.",
            wraplength=400
        ).grid(column=1, row=2, pady=10, sticky=tk.W)

    def fetch_crypto_data(self):
        """Busca os dados das criptomoedas da API CoinGecko.

        Returns:
            list: Lista de dicionários contendo dados das criptomoedas.
        """
        url = "https://api.coingecko.com/api/v3/coins/markets"
        parameters = {
            "vs_currency": "brl",
            "order": "market_cap_desc",
            "per_page": 15,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(url, params=parameters)
        data = response.json()
        return data

    def create_treemap(self, data):
        """Cria e exibe um gráfico do tipo Tree Map usando dados das criptomoedas.

        Args:
            data (list): Dados das criptomoedas.
        """
        # Extraindo os dados necessários para o gráfico
        df = pd.DataFrame(data)
        df = df[['name', 'market_cap', 'price_change_percentage_24h']]
        df.rename(columns={'price_change_percentage_24h': 'change'}, inplace=True)

        # Formatação dos valores para o gráfico (não na DataFrame)
        df['market_cap'] = df['market_cap'] / 1e9  # Convertendo para bilhões de BRL
        df['market_cap'] = df['market_cap'].round(2)

        fig = px.treemap(df, path=['name'], values='market_cap',
                         color='change',
                         color_continuous_scale='RdYlGn',
                         title='Market Cap and 24h Change of Cryptocurrencies')

        fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))

        fig.show()

    def on_show_treemap(self):
        """Callback para o botão que mostra o Tree Map."""
        data = self.fetch_crypto_data()
        self.create_treemap(data)

if __name__ == "__main__":
    # Criação da raiz da interface Tkinter
    root = tk.Tk()
    # Instanciação da classe CryptoAnalyzer
    app = CryptoAnalyzer(root)
    # Início do loop principal da interface gráfica
    root.mainloop()
