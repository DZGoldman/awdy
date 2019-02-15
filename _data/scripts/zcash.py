from coinscrapper import CoinScrapper

class ZCash(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'zcash'
        self.driver = driver
        

    def get_public_nodes(self):
        self.get_page("https://explorer.zcha.in/network")
        el = self.find_element("#count")
        print(el)
        return self.extract_first_int(el.text)
        
    def get_wealth_distribution(self):
        return 'n/a'

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        # TODO can't get from source (pie chart)
        return self.pool_stats_consensus_scrape()
