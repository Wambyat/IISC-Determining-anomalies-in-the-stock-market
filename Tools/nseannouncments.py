from nsepython import *
import pandas as pd

# specify the company ticker and date range
company_ticker = 'RELIANCE'
from_date = '01-01-2023'
to_date = '31-12-2023'

# get corporate filings and announcements for the specified company and date range
announcements = nse_announcements(symbol=company_ticker, from_date=from_date, to_date=to_date)

# convert the results to a pandas DataFrame
df = pd.DataFrame(announcements)

# display the results
print(df)