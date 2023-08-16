from nselib import capital_market

# comp = input("Company ticker: ")


# data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, from_date='06-06-2023', to_date='06-07-2023')
comp = 'ZURAISJNK'
data = capital_market.equity_list()
b = data.loc[data['SYMBOL']==comp]['NAME OF COMPANY']
try:
    print(b.values[0])
except IndexError:
    print("Invalid ticker <only nse is supported>")