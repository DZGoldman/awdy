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

    def get_client_codebases(self):
        self.get_page('https://coin.dance/nodes')
        count_containers = self.attempt_find_element( lambda: self.driver.find_elements_by_css_selector(".nodeCountBlock > h3 > .nodeTitle > strong"))
        all_counts = [int(container.text) for container in count_containers]
        client_codebases = self.get_cumulative_grouping_count(all_counts, .9)
        print('BTC codebases over 90%:', client_codebases)
        return client_codebases

    def get_consensus_distribution(self):
        self.get_page("https://www.blockchain.com/pools?timespan=24hours");

        # Other NOTE: "Unknown" is currently counted as a single pool (the biggest one in fact) potentially skewing the data
        table = self.attempt_find_element( lambda: self.driver.find_element_by_id("known_pools"))
        pools = self.read_table(table,converters={"count": int} )
        cumulative_sum = self.get_cumulative_grouping_count(pools['count'], 0.5)
        print('BTC pools with total > 50 % hashrate:', cumulative_sum)
        return int(cumulative_sum)
