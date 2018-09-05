from coinscrapper import CoinScrapper
import requests

class Ripple(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'ripple'
        self.driver = driver

    def get_public_nodes(self):
        try:
            # first try API
            res = requests.get('https://data.ripple.com/v2/network/topology/')
            public_nodes_count = res.json()['node_count']
            assert(isinstance(public_nodes_count, int))
            return public_nodes_count
        except:
            print('XRP api failed (xrp charts), falling back to web crawler:')
            self.get_page("https://xrpcharts.ripple.com/#/topology", sleep_time = 4)
            nodes_element = self.attempt_find_element( lambda: self.driver.find_element_by_class_name('nNodes'))
            public_nodes_count =  int(nodes_element.text)
            return public_nodes_count
        
    def get_wealth_distribution(self):
        try:
            # get sum of top 100 accounts
            res = requests.get('https://ledger.exposed/api/wallet-toplist/100/0')
            accounts = res.json()
            balance_sum = sum([account['Balance'] for account in accounts])

            # get total non-escrowed coin count:
            res = requests.get('https://ledger.exposed/api/richlist')
            data = res.json()['has']
            total_coins = sum([data[key]['balanceSum'] for key in data])
            wealth_distribution = balance_sum / total_coins
            assert(isinstance(wealth_distribution, float))
            
            # convert to %
            wealth_distribution = wealth_distribution * 100
            return wealth_distribution
            
        except:   
            print('XRP api failed (ledger exposed), falling back to web crawler:') 
            # in case api is down but site is still up? unlikely, but may as well try:
            self.get_page("https://ledger.exposed/rich-stats");
            wealth_distribution =  self.attempt_find_element( lambda:self.driver.find_element_by_css_selector('[data-v-ca88cbc2].large > b')).text
            wealth_distribution = self.percentage_string_to_float(wealth_distribution)
            return wealth_distribution
    def get_client_codebases(self):
        # A bit hard to get so leaving hard-coded for now; I suspect it won't be an issue any time soon ;)
        return 1

    def get_consensus_distribution(self):
        # N/A
        return 1
