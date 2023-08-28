from selenium import webdriver
import requests

WINDOW_SIZE = "1920,1080"
chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.nseindia.com/companies-listing/corporate-filings-announcements")
driver.get_screenshot_as_file("capture.png")
print(driver.get_cookies())
cookies = driver.get_cookies()
s = requests.Session()
print("setting cookies")
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])

print("cookie set.")

r = s.get("https://www.nseindia.com/api/corporate-announcements?index=equities&symbol=FOCUS")
print(r.text)

print("closing driver")
driver.quit()