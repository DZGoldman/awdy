from coinscrapper import CoinScrapper
class Nem(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'nem'
        self.driver = driver

    def get_public_nodes(self):
        self.get_page("https://nodeexplorer.com/")
        el = self.find_element('#nodesonline')
        return int(el.text)
        
    def get_wealth_distribution(self):
        self.get_page("https://nemnodes.org/richlist/")
        table = self.find_element('table')
        readtable = self.read_table(table, converters={"Percentage": self.percentage_string_to_float})
        value = readtable[readtable['Top Accounts'] == 'Top 100' ]['Percentage']
        return float(value)

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        return 'n/a'
