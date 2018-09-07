from coinscrapper import CoinScrapper

class SomeCoin(CoinScrapper):
'''
all methods should return ints, except wealth distribution, which can return a float
'''
    def __init__ (self, driver):
        self.name = 'somecoin'
        self.driver = driver

    def get_public_nodes(self):
        pass
        
    def get_wealth_distribution(self):
        pass

    def get_client_codebases(self):
        pass

    def get_consensus_distribution(self):
        pass
