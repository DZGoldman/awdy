from selenium import webdriver

import time, os
from bitcoin import Bitcoin
from ethereum import Ethereum 
from ripple import Ripple
from stellar import Stellar
from litecoin import Litecoin
from bitcoincash import BitcoinCash
from digibyte import Digibyte
from dogecoin import Dogecoin 
from monero import Monero
from neo import Neo 
from siacoin import Siacoin
from zcash import ZCash
from cardano import Cardano
from ardor import Ardor
from dash import Dash
from decred import Decred
from ethereumclassic import EthereumClassic 
from iota import Iota 
from nano import Nano
from nem import Nem
from qtum import Qtum 
from tezos import Tezos 
from vertcoin import Vertcoin 
from zencash import Zencash
from myriad import Myriad


# no macosx support for Xvfb, lazy develpment env solution:
if os.environ.get('AWDY_PROD'):
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(800, 800))  
    display.start()



options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("window-size=1024,768")
options.add_argument("--no-sandbox")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

start = time.time()
coins = [
    Bitcoin, 
    Ethereum, 
    Ripple,
    Litecoin,
    BitcoinCash, 
    Digibyte,
    Dash,
    Cardano,
    Iota,
    Nem,
    Vertcoin,
    Myriad,
    Neo,
    Tezos,
    Decred,
    Siacoin,
    
    
    # Incomplete:
    # Want:
    # ZCash,
    # Monero,
    # Dogecoin
    # EthereumClassic,
    # Stellar,


    # Nano,
    # Ardor,
    # Zencash,
    # Qtum,
    ]
for coin in coins:
    coin(driver).main(
        {
                'wealth_distribution': True,
                'public_nodes' : True,
                'consensus_distribution': True,
                'client_codebases': True
            }
    )

print('Scrape completed in ', time.time() - start)

driver.quit()

    # def get_all_coins (self):
    #     res = requests.get("https://api.coinmarketcap.com/v1/ticker/" params={
    #         'limit':300
    #     })
    #     return res.json()
    # def map_symbols_to_data(self, data):
    #     return {coin['symbol'].lower(): coin for coin in data}
