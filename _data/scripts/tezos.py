from coinscrapper import CoinScrapper
import time
class Tezos(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'tezos'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://tzscan.io/network")
        el = self.find_element('#Peer-title > span')
        return self.extract_first_int(el.text)
        
    def get_wealth_distribution(self):
        self.get_page('https://www.tezex.info/accounts')
        options = self.find_elements('option')
        # click option 100
        for option in options:
            if option.text == '100':
                option.click()
                time.sleep(3)
        table = self.find_element('.table')
        readtable = self.read_table(table, converters = {'Balance': lambda x: float(x.replace('ꜩ','').replace(',','').strip() )})
        total = readtable['Balance'].sum()
        # TODO: dynamic supply? (I think it's fixed)
        return 100 * total / 607489041 
    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        self.get_page("https://tzscan.io/rolls-distribution")
        table = self.find_element('.table')
        readtable = self.read_table(table, converters = {'Percent': self.percentage_string_to_float})
        cumulative_sum = self.get_cumulative_grouping_count(readtable['Percent'], .5)

        # TODO: make better
        tspans = self.find_elements('tspan')
        other_tag = [tspan for tspan in tspans if 'Others' in tspan.text]
        assert(len(other_tag)==1)
        other_text = other_tag[0].text.split(':')[1]
        unknown = round(self.percentage_string_to_float(other_text))

        return {
            'cumulative_sum': cumulative_sum,
            'unknown': unknown
        }

