from selenium import webdriver
import time, os, yaml


import importlib, inspect

import yaml, sys
if sys.argv[-1] == 'inp':
    config =  sys.argv[-2].split(',')
else:
    stream = open('config.yml', 'r')
    config = yaml.load(stream).copy()
    config = sorted([coin for coin in config if config[coin]])

coins = []
for coin_name in config:
    coin = importlib.import_module(coin_name) 
    for x in inspect.getmembers(coin):
        if x[0].lower() == coin_name:
            coins.append(x[1])
            break  


# no macosx support for Xvfb, lazy develpment env solution:
if os.environ.get('AWDY_PROD'):
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1024, 768))  
    display.start()



options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("window-size=1024,768")
options.add_argument("--no-sandbox")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

start = time.time()

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
