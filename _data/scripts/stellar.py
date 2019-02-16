from coinscrapper import CoinScrapper
import requests
# empty template for creating new coin, just for convenience
class Stellar(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'stellar'
        self.driver = driver

    def get_public_nodes(self):
        r = requests.get("https://api.stellarbeat.io/v1/nodes")
        nodes = r.json()
        return len([node for node in nodes if node.get('active')])
        # ???
        table =self.find_element('.table')
        table = self.find_element("#locations-table")
        readtable = self.read_table(table, converters={"Nodes": int})
        public_node_count = readtable['Nodes'].sum()
        return int(public_node_count)
        
    def get_wealth_distribution(self):
        # need source
        return 'n/a'

    def get_client_codebases(self):
        # https://www.stellarbeat.io/nodes
        return 1

    def get_consensus_distribution(self):
        return 1

