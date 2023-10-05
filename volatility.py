import numpy as np
from scipy.stats import norm

def black_scholes(option_type, S, K, T, r, sigma):
    """
    Calcula o preço de uma opção usando o modelo Black-Scholes.

    Parâmetros:
    - option_type: 'call' para opção de compra e 'put' para opção de venda.
    - S: Preço atual do ativo subjacente.
    - K: Preço de exercício da opção.
    - T: Tempo até a expiração da opção (em anos).
    - r: Taxa livre de risco (em decimal).
    - sigma: Volatilidade do ativo subjacente (em decimal).

    Retorna:
    O preço da opção.
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type deve ser 'call' ou 'put'.")

    return option_price

# Exemplo de uso:
option_type = 'call'  # Você pode escolher 'call' ou 'put'
S = 100  # Preço atual do ativo subjacente
K = 110  # Preço de exercício da opção
T = 1  # Tempo até a expiração da opção (em anos)
r = 0.05  # Taxa livre de risco
sigma = 0.2  # Volatilidade do ativo subjacente

opcao_preco = black_scholes(option_type, S, K, T, r, sigma)
print(f'O preço da opção {option_type} é: {opcao_preco:.2f}')