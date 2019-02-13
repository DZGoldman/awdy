import requests, time
from collections import defaultdict 
chainz_root = 'https://chainz.cryptoid.info/{symbol}/api.dws?q={query}'
class ReusableMethods():
    def _get_nodes_data_(self):
        # memoize to save an api call
        if not hasattr(self, 'nodes_result'):
            r = requests.get(chainz_root.format(symbol=self.symbol, query="nodes"))
            time.sleep(2)
            data = r.json()
            self.nodes_result = data
            return data
        else:
            return self.nodes_result 
    def cryptoid_api_nodes(self):
        data = self._get_nodes_data_()
        return sum( [len(d['nodes']) for d in data ] )

    def cryptoid_api_wealth_distribution(self):
        r = requests.get(chainz_root.format(symbol= self.symbol, query="rich"))
        time.sleep(2)
        data = r.json()
        total = data['total']
        rich_list = data['rich1000'][0:100]
        distribution = sum([wallet['amount'] for wallet in rich_list]) / total
        return distribution * 100

    def cryptoid_api_node_types(self):
        data = self._get_nodes_data_()
        mapping = defaultdict(int)
        for client in data:
            version = client['subver']
            client_name = version.split(':')[0] if ':' in version else version
            mapping[client_name] += len(client['nodes'])
        values = list(mapping.values())
        return self.get_cumulative_grouping_count(values, .9)

    def bitinfo_wealth_dist(self):
        # hack, ugle:
        name = "bitcoin cash" if self.name == 'bitcoincash' else self.name
        self.get_page("https://bitinfocharts.com/" + name)

        table = self.find_element('.table')
        read_table = self.read_table(table)
        values = read_table.values
        for row in values:
            if row[0] == 'Top 100 Richest':
                data = row[1]
                percentage_data = [self.percentage_string_to_float(word) for word in data.split() if '%' in word]
                return percentage_data[0]
    def chains_consensus_scrape(self):    
        self.get_page("https://chainz.cryptoid.info/{symbol}/#!extraction".format(symbol = self.symbol))
        table = self.find_element('#pools-share')
        read_table = self.read_table(table ,converters={"Last 1000": self.percentage_string_to_float})
        unknown =  int(read_table[read_table['Pool/Miner']=="All others" ]['Last 1000'])
        read_table = read_table[read_table['Pool/Miner']!="All others" ]
        
        cumulative_sum =  self.get_cumulative_grouping_count(read_table["Last 1000"], .5)

        return {
            'cumulative_sum': cumulative_sum,
            'unknown': unknown
        }

