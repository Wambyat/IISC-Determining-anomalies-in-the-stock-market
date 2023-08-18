from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
service = Service(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome(service=service, options=options)


url = "https://www.nseindia.com/api/corporate-announcements?index=equities"

# Go to the URL
driver.get(url)

# Get the source of the page
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Now you can use BeautifulSoup to find elements on the page
table = soup.find("table", {"id": "table"})
rows = table.find_all("tr")

for row in rows:
    cells = row.find_all("td")
    if len(cells) > 0:
        date = cells[0].text.strip()
        symbol = cells[1].text.strip()
        company_name = cells[2].text.strip()
        subject = cells[3].text.strip()
        print(f"{date} | {symbol} | {company_name} | {subject}")

# Close the browser
driver.quit()