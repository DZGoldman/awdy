from bitcoincash import BitcoinCash

# appropriately enough, BitcoinSV can inherit from Bitcoincash
class BitcoinSV(BitcoinCash):
    def __init__ (self, driver):
        self.name = 'bitcoinsv'
        self.driver = driver
        self.prefix = 'sv'

