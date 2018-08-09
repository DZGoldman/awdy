from coinscrapper import CoinScrapper


class Ripple(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'ripple'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://xrpcharts.ripple.com/#/topology", sleep_time = 4)
        nodes_element = self.attempt_find_element( lambda: self.driver.find_element_by_class_name('nNodes'))
        public_nodes_count =  int(nodes_element.text)
        print('XRP public nodes', public_nodes_count)
        return public_nodes_count
        
    def get_wealth_distribution(self):
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
