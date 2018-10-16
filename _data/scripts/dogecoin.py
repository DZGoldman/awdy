from coinscrapper import CoinScrapper

class Dogecoin(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'dogecoin'
        self.driver = driver

    def get_public_nodes(self):
        return 'n/a'
        
    def get_wealth_distribution(self):
        return self.bitinfo_wealth_dist()

    def get_client_codebases(self):
        return 'n/a'

    def get_consensus_distribution(self):
        # TODO can't get from source (pie chart)
        pass
