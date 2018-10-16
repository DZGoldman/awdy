from coinscrapper import CoinScrapper

# empty template for creating new coin, just for convenience
class Stellar(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'stellar'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://www.stellarbeat.io/");
        # ???
        table =self.find_element('.table')
        table = self.find_element("#locations-table")
        readtable = self.read_table(table, converters={"Nodes": int})
        public_node_count = readtable['Nodes'].sum()
        return int(public_node_count)
        
    def get_wealth_distribution(self):
        # TODO need source
        pass

    def get_client_codebases(self):
        # https://www.stellarbeat.io/nodes
        return 1

    def get_consensus_distribution(self):
        return 1

