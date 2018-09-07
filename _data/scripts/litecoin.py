from coinscrapper import CoinScrapper
from api_methods import CryptoidAPI

class Litecoin(CoinScrapper, CryptoidAPI):

    def __init__ (self, driver):
        self.name = 'litecoin'
        self.driver = driver
        self.symbol = 'ltc'

    def get_public_nodes(self):
        try:
            public_nodes_count = self.cryptoid_api_nodes()
            assert(isinstance(public_nodes_count, int))
            return public_nodes_count
        except:
            print('cryptoid api failed for LTC, falling back to scraper: ')
            self.get_page("https://chainz.cryptoid.info/ltc/#!network")
            table = self.attempt_find_element(lambda:  self.driver.find_element_by_id('network-clients'))
            # NOTE: table has a column withouth a header which offsets the other column by 1, so we need to use network share, not count
            readtable = self.read_table(table, converters = {"Network Share": float})
            public_nodes_count = int(readtable['Network Share'].sum())
            return public_nodes_count

    def get_wealth_distribution(self):
        return self.cryptoid_api_wealth_distribution()

    def get_client_codebases(self):
        return self.cryptoid_api_node_types()

    def get_consensus_distribution(self):
        self.get_page("https://www.litecoinpool.org/pools")
        # table is unlabled, but it's the second on that page:
        chart = self.attempt_find_element( lambda: self.driver.find_element_by_id('hashpie'))
        wedges = chart.find_elements_by_tag_name('g')
        data_sanitized = [self.percentage_string_to_float(w.text) for w in wedges if w.text]
        consensus_distribution = self.get_cumulative_grouping_count(data_sanitized, .5, target_sum = 100)
        return consensus_distribution
