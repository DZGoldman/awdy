from coinscrapper import CoinScrapper
from IPython import embed

class Qtum(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'qtum'
        self.driver = driver

    def get_public_nodes(self):
        # page not loading / too slow?
        print('getting public nodes')
        self.get_page("https://qtum.org/en", sleep_time=120)
        el = self.find_elements('.odomenter-value')
        print('?????????')
        print(el.text)
        
    def get_wealth_distribution(self):
        self.get_page('https://explorer.qtum.org/rich-list')
        els = self.find_elements('.centerMode.ng-binding')
        balance_strings = [el.text for el in els]
        # TODO lazy, imporove, add sanity checks
        balance_floats = [float(string.split(' ')[0].replace(',', '')) for string in balance_strings]
        top_100_total = sum(balance_floats[0:100])
        # TODO: dynamic?  circulating supply?
        total_supply = 100950944
        return 100 * top_100_total / total_supply
    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        pass
