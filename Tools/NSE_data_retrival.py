from nselib import capital_market

# comp = input("Company ticker: ")


# data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, from_date='06-06-2023', to_date='06-07-2023')
comp = 'ZURAISJNK'
data = capital_market.equity_list()
# only columns: SYMBOL, NAME OF COMPANY
data = data[['SYMBOL', 'NAME OF COMPANY']]
#convert to dict {SYMBOL: NAME OF COMPANY}
test = {data['SYMBOL'][i]: data['NAME OF COMPANY'][i] for i in range(len(data))}
# print(test)

# data = data.set_index('SYMBOL').T.to_dict('list')

# print(data)


# b = data.loc[data['SYMBOL']==comp]['NAME OF COMPANY']
try:
    print(test[comp])
except KeyError:
    print("Invalid ticker <only nse is supported>")