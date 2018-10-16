from coinscrapper import CoinScrapper

class Zencash(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'zencash'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://securenodes.eu.zensystem.io/")
        return int(
            self.find_element('#rup').text
        )
        
    def get_wealth_distribution(self):
        return 'n/a'

    def get_client_codebases(self):
       # TODO can't get from source (pie chart)
        return 1

    def get_consensus_distribution(self):
        pass
