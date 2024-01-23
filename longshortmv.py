import numpy as np
import pandas as pd
import statsmodels.api as sm
import yfinance as yf

# Baixa os dados históricos dos preços dos ativos BBDC3.SA e IGTI11.SA
bbdc3_data = yf.download("BBDC3.SA", start="2022-01-01", end="2024-01-01")
igti11_data = yf.download("IGTI11.SA", start="2022-01-01", end="2024-01-01")

# Use os preços de fechamento ajustados para dividendos e divisões
bbdc3_prices = bbdc3_data['Adj Close']
igti11_prices = igti11_data['Adj Close']

# Verifica se há valores nulos ou infinitos nos dados
if bbdc3_prices.isnull().any() or igti11_prices.isnull().any() or np.isinf(bbdc3_prices).any() or np.isinf(igti11_prices).any():
    print("Os dados contêm valores nulos ou infinitos. Corrija isso antes de prosseguir.")
else:
    # Garante que as séries temporais têm o mesmo índice
    bbdc3_prices, igti11_prices = bbdc3_prices.align(igti11_prices, join='inner')

    # Calcula a diferença logarítmica entre os preços dos ativos
    spread = np.log(bbdc3_prices) - np.log(igti11_prices)

    # Cria o DataFrame para a regressão
    data = pd.DataFrame({'spread_lagged': spread.shift(1), 'spread_diff': spread.diff()})
    data = data.dropna()  # Remove linhas com valores NaN resultantes das operações acima

    # Aplica a regressão linear para calcular a meia-vida
    model = sm.OLS(data['spread_diff'], sm.add_constant(data['spread_lagged'])).fit()
    halflife = -np.log(2) / model.params['spread_lagged']

    print("Meia-vida da estratégia long-short:", halflife)