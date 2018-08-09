from selenium import webdriver

from bitcoin import Bitcoin
from ethereum import Ethereum 
from ripple import Ripple

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1200x600")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

bitcoin = Bitcoin(driver)
bitcoin.main()

eth = Ethereum(driver)
eth.main()


rip = Ripple(driver)
rip.main()

driver.quit()
