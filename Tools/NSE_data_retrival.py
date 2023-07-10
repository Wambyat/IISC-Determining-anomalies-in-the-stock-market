from nselib import capital_market
import pandas
import nselib

comp = input("Company ticker: ")


data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, from_date='06-06-2023', to_date='06-07-2023')
print(data)