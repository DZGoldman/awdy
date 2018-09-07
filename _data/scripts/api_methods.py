import requests, time
from coinscrapper import CoinScrapper
from collections import defaultdict 

chainz_root = 'https://chainz.cryptoid.info/{symbol}/api.dws?q={query}'
class CryptoidAPI():
    def _get_nodes_data_(self, symbol):
        # memoize to save an api call
        if not hasattr(self, 'nodes_result'):
            r = requests.get(chainz_root.format(symbol=symbol, query="nodes"))
            time.sleep(2)
            data = r.json()
            self.nodes_result = data
            return data
        else:
            return self.nodes_result 
    def cryptoid_api_nodes(self, symbol):
        data = self._get_nodes_data_(symbol)
        return sum( [len(d['nodes']) for d in data ] )

    def cryptoid_api_wealth_distribution(self, symbol):
        r = requests.get(chainz_root.format(symbol=symbol, query="rich"))
        time.sleep(2)
        data = r.json()
        total = data['total']
        rich_list = data['rich1000'][0:100]
        distribution = sum([wallet['amount'] for wallet in rich_list]) / total
        return distribution * 100

    def cryptoid_api_node_types(self, symbol):
        data = self._get_nodes_data_(symbol)
        mapping = defaultdict(int)
        for client in data:
            version = client['subver']
            client_name = version.split(':')[0] if ':' in version else version
            mapping[client_name] += len(client['nodes'])
        values = list(mapping.values())
        return self.get_cumulative_grouping_count(values, .9)
