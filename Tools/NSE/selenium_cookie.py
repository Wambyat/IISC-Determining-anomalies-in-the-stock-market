from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys, os

# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')
print("hi")
blockPrint()
print("hello")
WINDOW_SIZE = "1920,1080"
chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/companies-listing/corporate-filings-announcements")
driver.get_screenshot_as_file("capture.png")
driver.quit()