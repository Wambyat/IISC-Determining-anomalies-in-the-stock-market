from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

WINDOW_SIZE = "1920,1080"
chrome_options = webdriver.ChromeOptions()
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'    
chrome_options.add_argument('user-agent={0}'.format(user_agent))
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
# service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()
while(True):
    driver.get("https://www.nseindia.com/companies-listing/corporate-filings-announcements")
    cookieList = driver.get_cookies()
    print([cookie['name'] for cookie in cookieList])
    if ['bm_sv','bm_mi','nseappid','_ga','nsit'] in [cookie['name'] for cookie in cookieList]:
        break
    else:
        driver.delete_all_cookies()
        driver.refresh()
        print("again")
        time.sleep(5)
cookieList = [i for i in cookieList if i['name'] == 'bm_sv' or i['name'] == 'bm_mi' or i['name'] == 'nseappid' or i['name'] == '_ga' or i['name'] == 'nsit']
print(cookieList)
'''
t = cookieList[0]['expiry']
print()
print('bm_sv=D60CFFC4E602F75CE7B0DCACAFB9D627~YAAQ5S/JFzpoS/2JAQAAr/l8IRSqkgL0329FFfgvJxrVSSV7+II+4M2EXOSsq33U0qPE+vVnlrsOgKxRN3A80eCEt203sSttATu81gQOi2F9uPeC35ZiVDQQwGqxvJBEnKgDHVv2PkPHuRSesKNa488m3jBz4kcnunv+5iPJ8IG4TQYxlpQOKAlrVbYR5Hsvz8AszX11hknSbaps7FBdSSY7yQHrJqzyY5aop/BITBTQ7H63UW3r3yQaKEeMFAqWOuTOcw==~1; Domain=.nseindia.com; Path=/; Expires=Wed, 23 Aug 2023 09:28:20 GMT; Max-Age=3947; Secure')
print()
print("mock below:\n\n\n")

print('bm_sv='+cookieList[0]['value']+'; Domain=.nseindia.com; Path=/; Expires='+time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime(t))+'; Max-Age=6194; Secure')
# driver.get_screenshot_as_file("capture.png")
while (True):
    pass
driver.quit()
'''