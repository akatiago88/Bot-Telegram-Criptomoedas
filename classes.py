import requests


class CoinGeckoAPI:
    def __init__(self, url_base: str):
        self.url_base = url_base

    def ping(self) -> bool:
        print('Verificando se a API esta online...')
        url = f'{self.url_base}/ping'
        return requests.get(url).status_code == 200

    def consulta_preco(self, id_moeda: str) -> tuple:
        print(f'Consultando preço da moeda de ID = {id_moeda}...')
        url = f'{self.url_base}/simple/price?ids={id_moeda}&vs_currencies=USD&include_last_updated_at=true'
        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados_moeda = resposta.json().get(id_moeda, None)
            preco = dados_moeda.get('usd', None)
            atualizado_em = dados_moeda.get('last_updated_at', None)

            return preco, atualizado_em

        else:
            raise ValueError('Código de resposta diferente de HTTP 200 OK')
