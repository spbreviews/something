import requests
from web3 import Web3
from config import networks, tokens

address = ''

# Функция для получения цены токена в USD
def get_price(token):
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={token}USDT')
    return float(response.json()['price'])

# Получите баланс для каждой сети
for network, rpc_url in networks.items():
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    balance = w3.eth.get_balance(address) # Это возвращает баланс в wei
    balance_in_token = w3.from_wei(balance, 'ether') # Это конвертирует баланс в токен

    token = tokens[network]
    price = get_price(token)
    balance_in_usd = round(float(balance_in_token) * price, 2)
    balance_in_token = round(float(balance_in_token), 3)

    print(f'Balance on {network}: {balance_in_token} {token} (${balance_in_usd})')
