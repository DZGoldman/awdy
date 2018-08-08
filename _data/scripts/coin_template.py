from coinscrapper import CoinScrapper

# empty template for creating new coin, just for convenience
class SomeCoin(CoinScrapper):

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
