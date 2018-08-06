from coinscrapper import CoinScrapper

class Bitcoin(CoinScrapper):
    def __init__ (self, driver):
        self.name = 'bitcoin'
        self.driver = driver
    def get_public_nodes(self):
        self.get_page("https://coin.dance/nodes");
        node_count_container = self.attempt_find_element( lambda: self.driver.find_element_by_css_selector("[title].nodeTitle > strong"))
        public_nodes_source = node_count_container.text
        print('BTC node count:', public_nodes_source)   
        return public_nodes_source
        
    def get_wealth_distribution(self):
        self.get_page("https://bitinfocharts.com/bitcoin/");
        # # Get data from page
        wealth_text = self.attempt_find_element( lambda: self.driver.find_element_by_id("tdid18")).text
        cleaned_text = wealth_text.replace(" ", "").split('/')
        wealth_distribution = cleaned_text[1]
        wealth_distribution = self.percentage_string_to_float(wealth_distribution)
        wealth_distribution = str(round(wealth_distribution)) + '%'
        print('BTC % money held by 100 accounts:', wealth_distribution)
        return wealth_distribution