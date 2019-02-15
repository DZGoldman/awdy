from coinscrapper import CoinScrapper

class Monero(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'monero'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://monerohash.com/nodes-distribution.html")
        el = self.find_element("#total-nodes").text
        return int(el)
        
    def get_wealth_distribution(self):
        return 'n/a'

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        return self.pool_stats_consensus_scrape(base_unit='H')
