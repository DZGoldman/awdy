# awdy
are we decentralized yet? an analysis of how truly decentralized cryptocurrency networks are

### contributing

all coin data is held in YAML files in the `_data/coins` directory: https://github.com/ummjackson/awdy/tree/master/_data/coins

to contribute, submit a PR with a new or edited .yml file and make sure to include credible sources. pull requests lacking sources for numbers 
will not be merged.

TODO change siacoin file name
change ardor file name / add file

blockers:
- qtum:
        - consensus: where is this data?
        - nodes: slow page loading?
- eth classic:
        - wealth and nodes not listed (on awdy) currently
        - codebases - can't find on page (pie chart)
- dogecoinL
        - consensus: pie chart, can't get
- monero
        - consensus: pdf
- zencash
        - consensus: pie
        - clients: lists 3, but links to zencash foundation with just 1?
zcash
        - consensus: pie chart
stellar
        - wealth not avaialble
ardor:
        - consensus not listed
*** CHANGED SOURCE ****
Vertcoin: used chainz for all



        # self.get_page("https://bitinfocharts.com/top-100-richest-bitcoin%20cash-addresses.html");

        # # # Get data from page
        # tables =  self.attempt_find_element( lambda: self.driver.find_elements_by_css_selector("#tblOne, #tblOne2"))
        # rows = []
        # for table in tables:
        #         rows += table.find_elements_by_css_selector('tr')
        # # # find % row
        # percentages = []
        # for row in rows[1:]:
        #     columns = row.find_elements_by_css_selector('td')
        #     percentages.append(float(columns[3].get_attribute('data-val')))
        # wealth_distribution = sum(percentages)

        # print('BCH % money held by 100 accounts:', wealth_distribution)
        # return wealth_distribution