from coinscrapper import CoinScrapper
class Nano(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'nano'
        self.driver = driver
    # NOTE: these may be a bit too ad hoc
    def get_public_nodes(self):
        self.get_page('https://nanocrawler.cc/status', sleep_time=3)
        els = self.find_elements('.text-muted')
        peer_el = [el for el in els if el.text == 'Peers'][0]
        parent = peer_el.find_element_by_xpath('..')  
        return self.extract_first_int(parent.text)

    def get_wealth_distribution(self):
        self.get_page('https://nanocrawler.cc/explorer/top_accounts', sleep_time=3)
        els = self.find_elements('.text-dark')
        el = [el for el in els if "total supply" in el.text][0]
        return self.extract_first_int(el.text)

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        self.get_page('https://mynano.ninja/active')
        # Note: this may be too vague
        data = self.find_elements('.h1')
        percentages = [self.percentage_string_to_float(el.text) for el in data]
        return self.get_cumulative_grouping_count(percentages, .5)

