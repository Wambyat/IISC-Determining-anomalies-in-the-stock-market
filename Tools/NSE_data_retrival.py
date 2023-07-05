from nselib import capital_market
import pandas

data = capital_market.price_volume_and_deliverable_position_data(symbol='SBIN', from_date='01-06-2023', to_date='10-06-2023')
print(data)