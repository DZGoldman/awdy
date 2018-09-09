from coinscrapper import CoinScrapper

class Myriad(CoinScrapper):
    '''
    all methods should return ints, except wealth distribution, which can return a float
    '''
    def __init__ (self, driver):
        self.name = 'myriad'
        self.driver = driver
        self.symbol = 'xmy'

    def get_public_nodes(self):
            return self.cryptoid_api_nodes()
            
    def get_wealth_distribution(self):
        return self.cryptoid_api_wealth_distribution()

    def get_client_codebases(self):
        return self.cryptoid_api_node_types() 

    def get_consensus_distribution(self):
        return self.chains_consensus_scrape()
