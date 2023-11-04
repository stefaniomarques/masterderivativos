import pandas as pd
import requests

#https://opcoes.net.br/listaopcoes/completa?cache=2023-11-4_10h6&au=True&uinhc=-20477038&idLista=ML&idAcao=PETR4&listarVencimentos=false&cotacoes=true&vencimentos=2023-12-15

# One maturity
def optionchaindate(subjaceente, vencimento):
    url = f'https://opcoes.net.br/listaopcoes/completa?idAcao=(subjacente)&listarVencimentos=false&cotacoes=true&vencimentos=(vencimento)'
    r = requests.get(url).json()
    