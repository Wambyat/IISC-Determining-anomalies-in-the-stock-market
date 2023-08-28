url = "https://www.nseindia.com/companies-listing/corporate-filings-announcements"

from seleniumwire import webdriver  # Import from seleniumwire  

# Create a new instance of the Firefox driver  
driver = webdriver.Chrome()  

# Go to the Google home page  
driver.get(url)  

# Access and print requests via the `requests` attribute  
for request in driver.requests:  
    if request.response:
        if request.url.startswith("https://www.nseindia.com/api/"):
            print(request.url)
            print(request.response.headers)
            print(request.response.body)
		# print(  
		# 	request.url,  
		# 	request.response.status_code,  
		# 	request.response.headers['Content-Type']) 