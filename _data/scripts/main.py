from selenium import webdriver

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

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1200x600")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

for coin in [
    Bitcoin, 
    Ethereum, 
    Ripple,
    Litecoin,
    BitcoinCash, 
    # Digibyte,
    # Stellar,
    # Dogecoin
    # Monero,
    # Neo,
    # Siacoin,
    # ZCash,
    # Cardano,
    # Ardor,
    # Dash,
    # Decred,
    # EthereumClassic,
    # Iota,
    # Nano,
    # Nem,
    # Qtum,
    # Tezos ,
    # Vertcoin,
    # Zencash,
    ]:
    coin(driver).main()


driver.quit()
