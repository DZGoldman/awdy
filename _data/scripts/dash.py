from coinscrapper import CoinScrapper

class Dash(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'dash'
        self.driver = driver
        self.symbol = 'dash'
    def get_public_nodes(self):
        # Page is slow, give it some extra time
        self.get_page("https://www.dashninja.pl/masternodes.html", sleep_time = 5)
        node_count = self.find_element('#mnactive').text
        return int(node_count)
    def get_wealth_distribution(self):
        return self.bitinfo_wealth_dist()

    def get_client_codebases(self):
        # https://www.dashninja.pl/masternodes.html, only 1
        return 1

    def get_consensus_distribution(self):
        return self.chains_consensus_scrape()

