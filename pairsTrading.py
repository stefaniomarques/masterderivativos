
import os
import pandas as pd
import itertools
import statsmodels.api as sm
import yfinance as yf
from math import factorial
from statsmodels.tsa.stattools import adfuller

# Símbolos das ações desejadas
acoes = ["BBAS3.SA", "BBDC4.SA"]  # Substitua pelos símbolos das ações que deseja analisar

# Obtém os dados das ações do Yahoo Finance
dados_acoes = yf.download(acoes, start="2022-01-01", end="2022-12-31")

# Calcula o número de ações
n = len(dados_acoes.columns) - 1

# Calcula o número de pares possíveis
npares = factorial(n) / (factorial(n - 2) * 2)

# Cria um DataFrame para armazenar os resultados
colunas = ["N", "Acao1", "Acao2", "PP1", "PP2", "PPR", "Alfa", "Beta", "Preco1", "Preco2", "Max", "Min", "DesvioP", "DesvioAb"]
pares = pd.DataFrame(columns=colunas)

# Inicializa o contador
z = 0

# Loop para calcular os resultados para cada par de ações
for i, j in itertools.combinations(dados_acoes.columns[:-1], 2):
    z += 1
    y = dados_acoes[i]
    x = dados_acoes[j]

    # Teste de estacionariedade Phillips-Perron
    pp_test_y = adfuller(y)
    pp_test_x = adfuller(x)

    # Regressão linear
    X = sm.add_constant(x)
    model = sm.OLS(y, X).fit()
    
    pares.loc[z] = [z, i, j, pp_test_y[1], pp_test_x[1], pp_test_y[1], model.params[0], model.params[1],
                    dados_acoes.iloc[-1][i], dados_acoes.iloc[-1][j], model.resid.max(), model.resid.min(),
                    model.resid.std(), dados_acoes.iloc[-1][i] - model.params[0] - model.params[1] * dados_acoes.iloc[-1][j]]

# Salva os resultados em um arquivo Excel usando pandas
pares.to_excel("resultados.xlsx", index=False)

# Salva os resultados em um arquivo CSV
pares.to_csv("resultados.csv", sep=";", decimal=".", index=False)