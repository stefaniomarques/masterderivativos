import pandas as pd
import yfinance as yf

# Coleta de dados históricos dos ativos e do índice de mercado (IBOV)
acao1 = yf.download('CSMG3.SA', start='2023-01-01', end='2023-10-31')
acao2 = yf.download('SAPR11.SA', start='2023-01-01', end='2023-10-31')
ibov = yf.download('^BVSP', start='2023-01-01', end='2023-10-31')

# Calculando os retornos diários
acao1['Retorno'] = acao1['Adj Close'].pct_change()
acao2['Retorno'] = acao2['Adj Close'].pct_change()
ibov['Retorno'] = ibov['Adj Close'].pct_change()

# Calculando a covariância entre os ativos e o mercado (IBOV)
cov_01 = acao1['Retorno'].cov(ibov['Retorno'])
cov_02 = acao2['Retorno'].cov(ibov['Retorno'])

# Calculando a variância do mercado (IBOV)
variance_ibov = ibov['Retorno'].var()
variance_acao2 = acao2['Retorno'].var()

# Calculando os betas
beta_acao1 = cov_01 / variance_ibov
beta_acao2 = cov_02 / variance_ibov

beta_acao3 = cov_01 / variance_acao2

print(f'Beta de CSMG3.SA em relação ao IBOV: {beta_acao1}')
print(f'Beta de SAPR11.SA em relação ao IBOV: {beta_acao2}')
print(f'Beta de CSMG3.SA em relação ao SAPR11.SA: {beta_acao3}')