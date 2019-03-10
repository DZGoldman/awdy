from coinscrapper import CoinScrapper
import requests

class Nano(CoinScrapper):

    def __init__ (self, driver):
        self.name = 'nano'
        self.driver = driver

    def get_public_nodes(self):
        res = requests.get('https://api.nanocrawler.cc/peer_count')
        return res.json()['peerCount']


    def get_wealth_distribution(self):
        data = requests.get('https://api.nanocrawler.cc/accounts/1').json()['accounts'] + requests.get('https://api.nanocrawler.cc/accounts/2').json()['accounts']
        assert(len(data)== 100)
        total =  sum( [float(d['balance']) for d in data] )
        return 100*total/133248289

    def get_client_codebases(self):
        return 1

    def get_consensus_distribution(self):
        res = requests.get('https://repnode.org/api/adjusted-nakamoto')
        return res.json()['adjusted_nakamoto_online']

