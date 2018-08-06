from bitcoin import Bitcoin
from ethereum import Ethereum 
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1200x600")

# Start driver with specified options
driver = webdriver.Chrome(chrome_options=options) 

bitcoin = Bitcoin(driver)
bitcoin.main()

eth = Ethereum(driver)
eth.main()

driver.quit()
