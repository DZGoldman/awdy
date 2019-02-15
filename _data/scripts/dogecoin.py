from coinscrapper import CoinScrapper
import requests 

class Dogecoin(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'dogecoin'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://www.coinexchange.io/network/peers/DOGE")
        els = self.find_elements('h4.animated-title')
        node_els = [el for el in els if "Active Peers" in el.text]
        assert(len(node_els) == 1)
        count = self.extract_first_int(node_els[0].text)
        return count
        
    def get_wealth_distribution(self):
        return self.bitinfo_wealth_dist()

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        # TODO can't get from source (pie chart)
        res = requests.get('https://chain.so/api/v2/block/DOGE/miners')
        data = res.json()['data']
        percent_data = [data[key] for key in data]
        return self.get_cumulative_grouping_count(percent_data, 0.5)
