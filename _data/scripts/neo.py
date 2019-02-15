from coinscrapper import CoinScrapper
import time
from collections import defaultdict
class Neo(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'neo'
        self.driver = driver
        self.live_nodes_memo = []

    def live_public_nodes(self):
        # this gets called twice and takes a while, so memoize:
        if len(self.live_nodes_memo):
            return self.live_nodes_memo

        self.get_page("http://monitor.cityofzion.io/")
        table = self.find_element('.stats-table')
        readtable = self.read_table(table, converters={'Is It Up?': lambda x: True if x == 'yes' else False})
        max_nodes_seen =  len(readtable['Is It Up?'][readtable['Is It Up?']])
        count = 0
        # nodes load dynamically, so repeat until there are no new ones 6 iterations in a row. Upper bound of 60 tries so we're not here all day
        for _ in range(60):
            table = self.find_element('.stats-table')
            readtable = self.read_table(table, converters={'Is It Up?': lambda x: True if x == 'yes' else False})
            new_max_nodes_seen = len(readtable['Is It Up?'][readtable['Is It Up?']])
            print('NEO lives nodes in sight:', new_max_nodes_seen)
            if new_max_nodes_seen <= max_nodes_seen:
                count+=1
            else:
                count = 0
                max_nodes_seen = new_max_nodes_seen
            if count == 6:
                break
            time.sleep(1)
        self.live_nodes_memo = readtable
        return readtable[readtable['Is It Up?']]

    def get_public_nodes(self):
        self.get_page("http://monitor.cityofzion.io/")
        live_public_nodes = self.live_public_nodes()
        return len(live_public_nodes)

    def get_wealth_distribution(self):
        self.get_page("https://coranos.github.io/neo/charts/neo-account-data.html", sleep_time = 5)

        # load only 100th element
        start_el = self.find_element('#startRowNbr')
        start_el.clear()
        start_el.send_keys('100')
        
        end_el = self.find_element('#endRowNbr')
        end_el.clear()
        end_el.send_keys('100')

        self.driver.execute_script('loadRows()')
        time.sleep(5)

        table = self.find_element("#dataTable")
        time.sleep(2)
        readtable = self.read_table(table, converters={'NEO Running Total, Percent': self.percentage_string_to_float})
        neo_col = float(readtable['NEO Running Total, Percent'])
        return neo_col
        

    def get_client_codebases(self):

        live_nodes = self.live_public_nodes()
        versions = live_nodes['Version'].apply(lambda version: version.split(':')[0].lower() if ':' in version else version)
        versions = versions[versions != '-']
        versions_count_map = defaultdict(int)
        for version in versions:
            versions_count_map[version]+=1
        versions_count = list(versions_count_map.values())
        return self.get_cumulative_grouping_count(versions_count, .9)
       

    def get_consensus_distribution(self):
        return 1
