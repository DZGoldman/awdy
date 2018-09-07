from coinscrapper import CoinScrapper

class Cardano(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'cardano'
        self.driver = driver

    def get_public_nodes(self):
        return 1
        
    def get_wealth_distribution(self):
        self.get_page("https://adatracker.com/richest")
        table = self.find_element('.table')
        read_table = self.read_table(table, converters = {"Share": self.percentage_string_to_float})
        wealth_share = read_table['Share']
        return wealth_share.sum()
    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        return 1
