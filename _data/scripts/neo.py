from coinscrapper import CoinScrapper

class Neo(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'neo'
        self.driver = driver

    def get_public_nodes(self):
        pass
        
    def get_wealth_distribution(self):
        pass

    def get_client_codebases(self):
        pass

    def get_consensus_distribution(self):
        pass
