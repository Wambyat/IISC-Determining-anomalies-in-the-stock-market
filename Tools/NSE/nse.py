from nselib import capital_market
import datetime
import time

comp = "MARUTI"
data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, period="1y")
# convert to json and print
# keep col Date and ClosePrice
data = data[["Date", "ClosePrice"]]
# convert data col into unix timestamp. format: 01-Jan-2020
data["Date"] = data["Date"].apply( lambda x: time.mktime(datetime.datetime.strptime(x, "%d-%b-%Y").timetuple()) )
#rename date to x and y ClosePrice to y
data = data.rename(columns={"Date": "x", "ClosePrice": "y"})
#convert y from str to float after removing , from y
data["y"] = data["y"].str.replace(",", "")
data["y"] = data["y"].astype(float)
data = data.to_json(orient="records")

# print with decent formatting
import json

print(json.dumps(json.loads(data), indent=4, sort_keys=True))