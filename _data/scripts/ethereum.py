from coinscrapper import CoinScrapper
import json, re
import pandas as pd

class Ethereum(CoinScrapper):
    
    def __init__ (self, driver):
        self.name = 'ethereum'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://www.ethernodes.org/network/1");
        list_items = self.attempt_find_element( lambda: self.driver.find_elements_by_css_selector(".pull-right.text-muted"))
        # Get "total node" element (has 100% in text)
        total_node_text = [e.text for e in list_items if '(100%)' in e.text][0]
        # Extract count from string
        public_node_count= re.sub("[\(\[].*?[\)\]]", "", total_node_text).strip()
        print('Eth node count: ', public_node_count)
        return int(public_node_count)
        
    def get_wealth_distribution(self):
        self.get_page("https://etherscan.io/accounts/1?ps=100");
        # # Get data from page
        table = self.attempt_find_element( lambda: self.driver.find_element_by_css_selector(".table"))

        # Read table as dataframe, sanitizing % column to float
        readtable = self.read_table(table, converters = {"Percentage": self.percentage_string_to_float })
        # Sum of % column
        wealth_distribution = readtable['Percentage'].sum()
        print('ETH wealth distribution:', wealth_distribution)
        return round(float(wealth_distribution))

    def get_client_codebases(self):
        self.get_page("https://www.ethernodes.org/network/1");
        client_graph =  self.attempt_find_element( lambda: self.driver.find_element_by_class_name('ex-graph'))
        # Extract stringified json
        client_data_json_string = client_graph.get_attribute('data-value')
        # Convert to dictionary
        client_data_json = json.loads(client_data_json_string)
        # Convert to Dataframe
        client_data_df = pd.DataFrame(client_data_json)
        # Sort values (values are node counts)
        client_codebases = self.get_cumulative_grouping_count(client_data_df['value'], .9)
        print('Eth codebases count:', client_codebases)
        return client_codebases

    def get_consensus_distribution(self):
        self.get_page("https://etherscan.io/stat/miner?range=7&blocktype=blocks");
        table = self.attempt_find_element( lambda: self.driver.find_element_by_css_selector(".table"))
        # read table, sanitize percentage
        readtable = self.read_table(table, converters={"Percentage":self.percentage_string_to_float })
       
        consensus_distribution = self.get_cumulative_grouping_count(readtable['Percentage'], .5, target_sum = 100)

        print('Eth consensus distribution:', consensus_distribution)
        return consensus_distribution
