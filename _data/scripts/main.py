from selenium import webdriver
import time
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

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1200x600")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

start = time.time()
for coin in [
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
    Nano,
    Neo,
    Tezos,
    Decred,

    # Siacoin,
    
    # ZCash,
    # Stellar,
    # Ardor,

    # Zencash,
    # Monero,
    # Dogecoin
    # EthereumClassic,
    # Qtum,
    ]:
    coin(driver).main(
        {
                'wealth_distribution': True,
                'public_node_count' : True,
                'consensus_distribution': True,
                'client_codebases': True
            }
    )

print('Scrape completed in ', time.time() - start)

driver.quit()
