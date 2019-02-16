from coinscrapper import CoinScrapper
import requests
class Iota(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'iota'
        self.driver = driver

    def get_public_nodes(self):
        r = requests.get("https://api.iota-nodes.net/")
        return len(r.json())
        
    def get_wealth_distribution(self):
        total_supply = 2779.530283277761
        self.get_page("https://thetangle.org/statistics/richest-addresses")
        values = self.find_elements('.iota-value')
        values = [v.text.replace('Ti', '').strip() for v in values]
        top_100_total = sum([float(v) for v in values])
        return (top_100_total / total_supply) * 100

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        return 1
