import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin
import matplotlib.pyplot as plt

yfin.pdr_override()

vale_data = pdr.get_data_yahoo('VALE3.SA', start='2000-01-01', end='2023-08-01')

# Plotar um gráfico de preços de fechamento
plt.figure(figsize=(12, 6))
vale_data['Close'].plot()
plt.title('Preços de Fechamento da VALE3 (Jan 01, 2000 - Ago 01, 2023)')
plt.xlabel('Data')
plt.ylabel('Preço de Fechamento')
plt.grid(True)
plt.show()