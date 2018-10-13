from coinscrapper import CoinScrapper
import time

class Decred(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'decred'
        self.driver = driver
    def get_public_nodes(self):
        self.get_page("https://dcrstats.com/map")
        el = self.find_element('.decred-subtitle')
        count = self.extract_first_int(el.text)

        return count
    def get_wealth_distribution(self):
        self.get_page('https://www.dcr.observer/')
        self.find_element('.show-all-500').click()
        time.sleep(3)
        table = self.find_element('.table-addresses')
        readtable = self.read_table(table, converters = {"Balance": self.extract_only_ints})
        top_100_sum = readtable[0:100]['Balance'].sum()
        total = self.extract_only_ints(
            self.find_element('.total-dcr').text
        )
        return 100 * top_100_sum / total

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        self.get_page("https://dcrstats.com/pow")
        table = self.find_element('#pools-table')
        readtable = self.read_table(table, converters = {"Network %": self.percentage_string_to_float})
        return self.get_cumulative_grouping_count(readtable["Network %"], .5)
