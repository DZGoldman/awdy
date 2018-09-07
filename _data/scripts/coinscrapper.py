import yaml
import time
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import numpy as np
from reusable_methods import ReusableMethods

class CoinScrapper(ReusableMethods):
    '''
    All coins will inherit from this class
    '''
    # constants:
    default_page_load_wait_time = 1

    def main(self):
        '''
        triggers all 4 data collection methods and writes to yml (good place to start if following logic of program)
        '''
        new_data_for_yml = {}
        try:
            wealth_distribution  = self.get_wealth_distribution()
            assert(0 < wealth_distribution <=100)
            new_data_for_yml['wealth_distribution'] = str( round(wealth_distribution,2 ) ) + '%'
        except Exception as e: 
            print('ERROR FINDING {} WEALTH DISTRIBUTION'.format(self.name))
            print(e)

        try:
            public_node_count  = self.get_public_nodes()
            assert(public_node_count >= 1)
            new_data_for_yml['public_nodes'] = public_node_count
        except Exception as e: 
            print('ERROR FINDING {} PUBLIC NODE COUNT'.format(self.name))
            print(e)
        
        try:
            client_codebases  = self.get_client_codebases()
            assert(client_codebases >= 1)
            new_data_for_yml['client_codebases'] = client_codebases
        except Exception as e: 
            print('ERROR FINDING {} CLIENT CODEBASES'.format(self.name))
            print(e)
        
         
        try:
            consensus_distribution  = self.get_consensus_distribution()
            assert(consensus_distribution >= 1)
            new_data_for_yml['consensus_distribution'] = consensus_distribution
        except Exception as e: 
            print('ERROR FINDING {} CONSENSUS DISTRIBUTION'.format(self.name))
            print(e)

        print('new data for yml for {}:'.format(self.name),new_data_for_yml)
        self.write_to_yml(new_data_for_yml)

    def write_to_yml(self, new_data):
        '''
        overwrites new values in new_data dictionary to yml file
        '''
        fname = "_data/coins/{}.yml".format(self.name.replace(' ', '-'))
        stream = open(fname, 'r')
        
        data = yaml.load(stream).copy()
        data.update(new_data)
        with open(fname, 'w') as yaml_file:
            yaml_file.write( yaml.dump(data, default_flow_style=False))


    # Methods below are 'helper methods' for crawling and sanitizing data
    def get_page(self, url, sleep_time = False):
        if self.driver.current_url != url:
            self.driver.get(url)
            self.sleep(sleep_time) 

    def sleep(self, sleep_time = False):
        time.sleep(sleep_time or self.default_page_load_wait_time)


    def find_element(self, css_selector, wait_time=10):
        '''
        Wrapper to use with 'find_element' methods. wait_time can be overridden for particularly persnickety cases.
        use : lib.attempt_find_element( lambda: find_element_by_id('#interesting_data'), driver = driver)
        '''
        # count_containers = self.attempt_find_element( lambda: self.driver.find_elements_by_css_selector(".nodeCountBlock > h3 > .nodeTitle > strong"))
        return WebDriverWait(self.driver, wait_time).until(lambda x: self.driver.find_element_by_css_selector(css_selector) )


    def find_elements(self, css_selector, wait_time=10):
        '''
        Wrapper to use with 'find_element' methods. wait_time can be overridden for particularly persnickety cases.
        use : lib.attempt_find_element( lambda: find_element_by_id('#interesting_data'), driver = driver)
        '''
        # count_containers = self.attempt_find_element( lambda: self.driver.find_elements_by_css_selector(".nodeCountBlock > h3 > .nodeTitle > strong"))
        return WebDriverWait(self.driver, wait_time).until(lambda x: self.driver.find_elements_by_css_selector(css_selector) )


    def percentage_string_to_float(self, st):
        return float(st.replace('%', '').strip())

    def get_cumulative_grouping_count(self, data, target_percentage, target_sum = False):
        '''
        accepts list or dataframe of numbers, where each number represents counts of categories. Returns minimum number of categories such that make up target_percentage of total. Total is calculated or passed in directly. (I hope this makes sense)
        '''
        if isinstance(data, list):
            data = pd.DataFrame(data)[0]
        # Sort values (values are node counts)
        sorted_data = data.sort_values(ascending=False)
        # Get series of percentages of total
        data_sum = target_sum or sorted_data.sum()
        cumulative_sum_percentages = sorted_data.cumsum() / data_sum
        # Find how many make > 90 %
        return  int(np.where(cumulative_sum_percentages.gt(target_percentage) )[0][0] +1)

    def read_table(self, table, converters={}):
        '''
        converts selenium table object to dataframe; open to transform data type of columns
        '''
        return pd.read_html(table.get_attribute("outerHTML"), header=0, converters=converters)[0]
