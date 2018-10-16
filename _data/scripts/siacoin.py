from coinscrapper import CoinScrapper
import requests
class Siacoin(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'siacoin'
        self.driver = driver

    def get_public_nodes(self):
        r = requests.get('https://siastats.info/dbs/activehosts.json')
        data = r.json()
        return data[-1]['hosts']
    def get_wealth_distribution(self):
        return 'n/a'

    def get_client_codebases(self):
        # TODO: make dynamic?
        return 1

    def get_consensus_distribution(self):
        self.get_page('https://siastats.info/mining_pools')
        percentages = []
        for i in range(9):
            try:
                el = self.find_element('#data{}4'.format(str(i)))
                percentages.append(self.percentage_string_to_float(el.text))
            except:
                pass
        # sanity
        assert(len(percentages) >= 7)
        return self.get_cumulative_grouping_count(percentages, 0.5, 100)
