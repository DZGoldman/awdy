from coinscrapper import CoinScrapper
import time
import pandas as pd
class Ardor(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'ardor'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page('https://ardor.tools/network')
        return int(
            self.find_element('.box').text
        )
        
    def get_wealth_distribution(self):
        self.get_page("https://ardor.tools/topAccounts")
        all_balances = pd.DataFrame()
        kill_switch = 0
        while len(all_balances) < 100:
            table = self.find_element('table')
            readtable = self.read_table(table)
            balances = readtable['Balance']
            all_balances = pd.concat( [all_balances, balances])
            next_button = self.find_element('.pagination-next')
            next_button.click()
            time.sleep(0.1)

            kill_switch += 1
            if kill_switch > 20:
                break

        top_100_total = float(all_balances[0:100].sum())
        total_suppy = 998999495
        return 100 * top_100_total / total_suppy
    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        # TODO need source
        pass
