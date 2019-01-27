import yaml, re, time, os, datetime
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import numpy as np
from reusable_methods import ReusableMethods

cwd = os.getcwd()

with open(cwd + '/log.log', 'a') as f:
    f.write('\n\nstart!\n')

class CoinScrapper(ReusableMethods):
    '''
    All coins will inherit from this class
    '''
    # constants:
    default_page_load_wait_time = 3

    def main(self, options = {}):
        options = {
            **{
                'wealth_distribution': True,
                'public_node_count' : True,
                'consensus_distribution': True,
                'client_codebases': True
            }, **options
        }
        '''
        triggers all 4 data collection methods and writes to yml (good place to start if following logic of program)
        '''
        new_data_for_yml = {}
        if options['wealth_distribution']:
            try:
                wealth_distribution  = self.get_wealth_distribution()
                if wealth_distribution == 'n/a':
                    new_data_for_yml['wealth_distribution'] = ''
                else:
                    assert(0 < wealth_distribution <=100)
                    new_data_for_yml['wealth_distribution'] = str( round(wealth_distribution,2 ) ) + '%'
                new_data_for_yml['wealth_distribution_la'] = time.strftime('%l:%M%p %Z on %b %d, %Y') 
            except Exception as e: 
                err = 'ERROR FINDING {} WEALTH DISTRIBUTION'.format(self.name) + ': ' + str(e)
                
                self.log(err)
                # logger.error(err)

        if options['public_node_count']:
            try:
                public_node_count  = self.get_public_nodes()
                if public_node_count == 'n/a':
                    new_data_for_yml['public_nodes'] = ''
                else:
                    assert(public_node_count >= 1)
                    new_data_for_yml['public_nodes'] = public_node_count
                new_data_for_yml['public_node_count_la'] = time.strftime('%l:%M%p %Z on %b %d, %Y') 
            except Exception as e: 
                err = 'ERROR FINDING {} PUBLIC NODE COUNT'.format(self.name) + ': ' + str(e)
                self.log(err)
        if options['client_codebases']:
            try:
                client_codebases  = self.get_client_codebases()
                if client_codebases == 'n/a':
                    new_data_for_yml['client_codebases'] = ''
                else:
                    assert(client_codebases >= 1)
                    new_data_for_yml['client_codebases'] = client_codebases
                new_data_for_yml['client_codebases_la'] = time.strftime('%l:%M%p %Z on %b %d, %Y') 
            except Exception as e: 
                err = 'ERROR FINDING {} CLIENT CODEBASES'.format(self.name) + ': ' + str(e)
                self.log(err)
        
        if options['consensus_distribution']:
            try:
                consensus_distribution  = self.get_consensus_distribution()
                if consensus_distribution == 'n/a':
                    new_data_for_yml['consensus_distribution'] = ''
                else:
                    assert(consensus_distribution >= 1)
                    new_data_for_yml['consensus_distribution'] = consensus_distribution
                new_data_for_yml['consensus_distribution_la'] = time.strftime('%l:%M%p %Z on %b %d, %Y') 
            except Exception as e: 
                err = 'ERROR FINDING {} CONSENSUS DISTRIBUTION'.format(self.name) + ': ' + str(e)
                self.log(err)

        print('new data for yml for {}:'.format(self.name),new_data_for_yml)
        self.write_to_yml(new_data_for_yml)

    def write_to_yml(self, new_data):
        '''
        overwrites new values in new_data dictionary to yml file
        '''
        fname = "_data/coins/{}.yml".format(self.name)
        stream = open(fname, 'r')
        
        data = yaml.load(stream).copy()
        data.update(new_data)
        with open(fname, 'w') as yaml_file:
            yaml_file.write( yaml.dump(data, default_flow_style=False))
            
    def read_from_yaml(self):
        '''
        overwrites new values in new_data dictionary to yml file
        '''
        fname = "_data/coins/{}.yml".format(self.name)
        stream = open(fname, 'r')
        data = yaml.load(stream).copy()
        return data


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
    
    def extract_only_ints(self, r):
        s = ''.join(x for x in r if x.isdigit())
        return int(s)

    def extract_first_int(self, string):
        return int(re.search(r'\d+', string).group())

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

    def log(self, message):
        print(message)
        message = str(datetime.datetime.now()) +': ' + message
        with open(cwd + '/log.log', 'a') as f:
            f.write(message + '\n')
# cwd = os.getcwd()
# print(cwd)
# logging.basicConfig(filename=cwd + '/errorlog.log', level=logging.DEBUG, 
#                     format='%(asctime)s %(levelname)s %(name)s %(message)s')
# logger=logging.getLogger(__name__)

