from coinscrapper import CoinScrapper
import pdb
class EthereumClassic(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'ethereum classic'
        self.driver = driver

    def get_public_nodes(self):
        return 'n/a'
        
    def get_wealth_distribution(self):
        return 'n/a'

    def get_client_codebases(self):
        # TODO can't get from source (pie chart)
        pass

    def get_consensus_distribution(self):
       
        self.get_page('https://gastracker.io/stats/miners')
        table = self.find_element('.table.stats')
        target_column = "Unnamed: 3"
        readtable = self.read_table(table)
        hashrate_percentages = readtable[target_column]
        # ugly: need to remove row title, inclue sanity check
        assert('Share' in hashrate_percentages[0])
        hashrate_percentages = hashrate_percentages[1:]
        # TODO: make sure target sum is given everywhere when needed
        return self.get_cumulative_grouping_count(hashrate_percentages.map(lambda x: float(x)), 0.5, 100)