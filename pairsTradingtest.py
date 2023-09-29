import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

symbol1 = "CSMG3.SA"  # Exemplo: Banco do Brasil
symbol2 = "SAPR11.SA"  # Exemplo: Itaú

start = "2022-01-01"
end = "2023-08-31"

data1 = yf.download(symbol1, start=start, end=end)['Adj Close']
data2 = yf.download(symbol2, start=start, end=end)['Adj Close']

df = pd.DataFrame({'Ação1': data1, 'Ação2': data2})

# Trate os dados brutos para preencher os valores ausentes com a média
df.fillna(df.mean(), inplace=True)

# Verifique e trate os dados brutos das séries antes da diferenciação
if df['Ação1'].isnull().any() or df['Ação2'].isnull().any():
    print("Existem valores ausentes nos dados brutos. Realize o tratamento adequado.")
else:
    # Realize a diferenciação para tornar as séries estacionárias
    df['Diff_Ação1'] = df['Ação1'].diff()
    df['Diff_Ação2'] = df['Ação2'].diff()
    
    # Preencha os valores NaN com a média das respectivas colunas
    df['Diff_Ação1'].fillna(df['Diff_Ação1'].mean(), inplace=True)
    df['Diff_Ação2'].fillna(df['Diff_Ação2'].mean(), inplace=True)

    # Realize o teste de Augmented Dickey-Fuller (ADF) para ambas as séries diferenciadas
    result1 = adfuller(df['Diff_Ação1'])
    result2 = adfuller(df['Diff_Ação2'])

    # Defina um nível de significância para o teste (por exemplo, 0,05)
    alpha = 0.05

    # Compare os resultados com o nível de significância
    if result1[1] < alpha and result2[1] < alpha:
        print(f"As ações {symbol1} e {symbol2} têm cointegração (têm tendência).")
    else:
        print(f"As ações {symbol1} e {symbol2} não têm cointegração (não têm tendência).")