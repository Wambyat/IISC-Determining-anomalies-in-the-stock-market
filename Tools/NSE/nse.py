from nselib import capital_market
import datetime

# comp = input("Company ticker: ")

today = datetime.date.today()
print(today.strftime("%d-%m-%Y"))
yesterday = today - datetime.timedelta(days=5)
print(yesterday)

comp = "FOCUS"
data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, from_date=yesterday.strftime("%d-%m-%Y"), to_date=today.strftime("%d-%m-%Y"))
print(data)
# comp = 'ZURAISJNK'
# data = capital_market.equity_list()
# # only columns: SYMBOL, NAME OF COMPANY
# data = data[['SYMBOL', 'NAME OF COMPANY']]
# #convert to dict {SYMBOL: NAME OF COMPANY}
# test = {data['SYMBOL'][i]: data['NAME OF COMPANY'][i] for i in range(len(data))}
# # print(test)

# # data = data.set_index('SYMBOL').T.to_dict('list')

# # print(data)


# # b = data.loc[data['SYMBOL']==comp]['NAME OF COMPANY']
# try:
#     print(test[comp])
# except KeyError:
#     print("Invalid ticker <only nse is supported>")