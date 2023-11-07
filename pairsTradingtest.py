import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

acoes = ["PETR4.SA", "TIMS3.SA"]

start = "2023-01-01"
end = "2023-08-31"

df = yf.download(acoes, start=start, end=end)['Adj Close']

df.isna().sum()

# Trate os dados brutos para preencher os valores ausentes com a média
df.fillna(df.mean(), inplace=True)

# Extrai do data frame uma coluna com iloc
acao1 = df.iloc[:,0]
acao1.head()
acao2 = df.iloc[:,1]
acao2.head()

#Test Philip-Perron hipótese nula (H0): A série temporal possui uma raiz unitária e é não estacionária.
pp = PhillipsPerron(acao1)
print(pp.summary().as_text())

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

# Teste de raiz unitária dos resíduos (PP)
pp = PhillipsPerron(residuos)
print(pp.summary().as_text())

# A série é cointegrada se apresentar P-valor abaixo de 0.10

# Apresentar séries no data frame em gráfico
df.plot()
plt.show()

# BBDC4 = -04,1373 + 0,7270 * ITUB4 (relação de equilíbrio)
bbdc4 = 14.30
itub4 = 27.21
diferenca = bbdc4 - (-4.1373 + 0.7270 * itub4)
diferenca

np.std(residuos) # desvio médio dos resíduos
max(residuos) # diferença máxima da média dos resíduos em módulo
min(residuos) # diferença mínima da média dos resíduos em módulo

'''
Processo Ornstein–Uhlenbeck
Teste de contagem para saber quantas vezes os pares cruzaram 0.00
Prepapar o loop para os outros ativos do IBOV
'''

# Calcular diferentes pares de ativos para uma série do IBOV
n_assets = 85
x = np.math.factorial(n_assets) / (np.math.factorial(n_assets - 2) * 2)
xyp-jani-qpk