import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

acoes = ["PETR4.SA", "TIMS3.SA"]

start = "2022-01-01"
end = "2023-08-31"

df = yf.download(acoes, start=start, end=end)['Adj Close']

df.isna().sum()

# Trate os dados brutos para preencher os valores ausentes com a média
df.fillna(df.mean(), inplace=True)

'''
Passo 1 Testar as duas séries para raiz unitária
Passo 2 Rodar OLS (Regressão Linear Simples)
Passo 3 Testar resíduos para tendência
'''

# Extrai do data frame uma coluna com iloc
acao1 = df.iloc[:,0]
acao1.head()
acao2 = df.iloc[:,1]
acao2.head()

#Teste ADF; hipótese nula (H0): A série temporal possui raiz unitária, ou seja, não é estacionária.
result_adf = sm.tsa.adfuller(acao1)
print("ADF Test Results:") 
print(f"Test Statistic: {result_adf[0]}")
print(f"P-value: {result_adf[1]}")
print(f"Critical Values: {result_adf[4]}")

#Test Philip-Perron hipótese nula (H0): A série temporal possui uma raiz unitária e é não estacionária.
pp = PhillipsPerron(acao1)
print(pp.summary().as_text())

#Teste ADF para ação 02
result_adf = sm.tsa.adfuller(acao2)
print("ADF Test Results:") 
print(f"Test Statistic: {result_adf[0]}")
print(f"P-value: {result_adf[1]}")
print(f"Critical Values: {result_adf[4]}")

# Teste PP para ação 02
pp = PhillipsPerron(acao2)
print(pp.summary().as_text())

# Regressão Linear Simples
acao2 = sm.add_constant(acao2)
model = sm.OLS(acao1, acao2).fit()

# Print a summary of the regression results
print(model.summary())

# Extrair os resíduos do modelo
residuos = model.resid
residuos.plot()
plt.show()

# Teste de raiz unitária dos resíduos (ADF E PP)
result_adf = sm.tsa.adfuller(residuos)
print("ADF Test Results:") 
print(f"Test Statistic: {result_adf[0]}")
print(f"P-value: {result_adf[1]}")
print(f"Critical Values: {result_adf[4]}")

pp = PhillipsPerron(residuos)
print(pp.summary().as_text())

# A série é cointegrada se apresentar P-valor abaixo de 0.10