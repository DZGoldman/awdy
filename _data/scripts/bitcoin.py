from coinscrapper import CoinScrapper

class Bitcoin(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'bitcoin'
        self.driver = driver
        
    def get_public_nodes(self):
        self.get_page("https://coin.dance/nodes");
        node_count_container = self.find_element("h3 > div[data-hasqtip] > strong")
        public_nodes_source = node_count_container.text
        return int(public_nodes_source)
        
    def get_wealth_distribution(self):
        self.get_page("https://bitinfocharts.com/bitcoin/");
        # Get data from page
        wealth_text = self.find_element("#tdid18").text
        cleaned_text = wealth_text.replace(" ", "").split('/')
        wealth_distribution = cleaned_text[1]
        wealth_distribution = self.percentage_string_to_float(wealth_distribution)
        return wealth_distribution

    def get_client_codebases(self):
        self.get_page('https://coin.dance/nodes')
        count_containers = self.find_elements(".nodeCountBlock > h3 > .nodeTitle > strong")
        # convert elements to list of integers, representing count of each codebase
        all_counts = [int(container.text) for container in count_containers]
        client_codebases = self.get_cumulative_grouping_count(all_counts, .9)
        return client_codebases

    def get_consensus_distribution(self):
        self.get_page("https://www.blockchain.com/pools?timespan=24hours");

        # Other NOTE: "Unknown" is currently counted as a single pool (the biggest one in fact) potentially skewing the data
        table = self.find_element("#known_pools")
        pools = self.read_table(table,converters={"count": int} )
        cumulative_sum = self.get_cumulative_grouping_count(pools['count'], 0.5)
        return cumulative_sum
