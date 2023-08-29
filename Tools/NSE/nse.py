from nselib import capital_market


comp = "FOCUS"
data = capital_market.price_volume_and_deliverable_position_data(symbol=comp, period="1W")
# convert to json and print
data = data.to_json(orient="records")

# print with decent formatting
import json

print(json.dumps(json.loads(data), indent=4, sort_keys=True))