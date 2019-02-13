from coinscrapper import CoinScrapper
class BitcoinCash(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'bitcoincash'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://cash.coin.dance/nodes");
        node_count_container = self.find_element("h3 > div[data-hasqtip] > strong")
        public_nodes_source = node_count_container.text
        return int(public_nodes_source)
        
    def get_wealth_distribution(self):
        return self.bitinfo_wealth_dist()


    def get_client_codebases(self):
        self.get_page("https://cash.coin.dance/nodes");
        count_containers = self.find_elements( ".nodeCountBlock > h3 > .nodeTitle > strong")
        all_counts = [int(container.text) for container in count_containers]
        client_codebases = self.get_cumulative_grouping_count(all_counts, .9)
        return client_codebases

    def get_consensus_distribution(self):
        self.get_page('https://cash.coin.dance/blocks/today')
        tspan_objects =  self.find_element( '#chartobject-1').find_elements_by_css_selector('tspan')
        a = []
        for span in tspan_objects:
            text = span.text
            if ',' in text:
                s = text.split(',')[1].replace('%', '').strip()
                if text.split(',')[0].strip() ==  'Other Mining Pools':
                    unknown = s
                else:
                    a.append(float(s))
        consensus_distribution = self.get_cumulative_grouping_count(a, .5)
        return {
            'cumulative_sum': consensus_distribution,
            'unknown': unknown
        }


