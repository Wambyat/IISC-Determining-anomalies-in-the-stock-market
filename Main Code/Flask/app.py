from flask import Flask, jsonify, request
from flask_cors import CORS
from nselib import capital_market
import datetime
import time

app = Flask(__name__)
app.config.from_object(__name__)
# We are doing this to allow vue to send requests to this flask server.
CORS(app, resources={r"/*": {"origins": "*"}})


# This is just a testing route. Use this to run sanity tests and whatever else.
@app.route("/", methods=["GET","POST"])
def home():
    return jsonify({"message": "This is a test message. From Flask."})


# This finds the stock in the list of stocks and returns the ticker and name. If the stock is not found, returns {"error": "Invalid ticker <only nse is supported>"}. 
# Only POST requests to this route. The post request should be of the form:
# {"search": "stock name"}
# It should be the exact name in this case. No need to improve this as there is the dynamic list.
@app.route("/api/search", methods=["POST"])
def search():

    try:
        post_data = request.get_json()
        search_query = post_data["search"].upper()
        data = capital_market.equity_list()
        
        # data has other columns too. We only need the name and ticker.
        data = data[["SYMBOL", "NAME OF COMPANY"]]
        all_company_dict = {
            data["SYMBOL"][i]: data["NAME OF COMPANY"][i] for i in range(len(data))
        }
        
        try:
            return jsonify({"name": all_company_dict[search_query], "ticker": search_query})
        
        except KeyError:
            return jsonify({"error": "Invalid ticker <only nse is supported>"})
    
    except Exception as e:
        return jsonify({"error": str(e)})


# This returns the list of all the stocks in the NSE. Only GET requests to this route.
# The response is of the form:
# {"ticker": "name"}
@app.route("/api/all", methods=["GET"])
def all():
    try:
        data = capital_market.equity_list()
        data = data[["SYMBOL", "NAME OF COMPANY"]]
        all_company_dict = {
            data["SYMBOL"][i]: data["NAME OF COMPANY"][i] for i in range(len(data))
        }
        return jsonify(all_company_dict)
    except Exception as e:
        return jsonify({"error": str(e)})


# This returns today's data of the stock. GET method is used here only for debugging and tests. POST method should be of the form:
# {"ticker": "stock ticker"}
# The response is of the form:
# {
#  "%DlyQttoTradedQty":<float>,
#  "AveragePrice":<float>,
# "ClosePrice":<float>,
# "Date":"dd-mmm-yyyy",
# "DeliverableQty":"<int>",
# "HighPrice":<float>,
# "LastPrice":<float>,
# "LowPrice":<float>,
# "No.ofTrades":"<int>",
# "OpenPrice":<float>,
# "PrevClose":<float>,
# "Series":"<str>",
# "Symbol":"<str>",
# "TotalTradedQuantity":"<int>",
# "TurnoverInRs":"<float>"
# }
#! all the values that say "<int>" can be like: "234" or "1,234". So filter out "," before any conversions.
@app.route("/api/stock/", methods=["POST", "GET"])
def stock():
    if request.method == "POST":
        comp = request.get_json()
        comp = comp["ticker"].upper()
    else:
        comp = "FOCUS"
    try:
        # We take a 5 day buffer to account for any long holidays or extended weekends.
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=5)
        data = capital_market.price_volume_and_deliverable_position_data(
            symbol=comp,
            from_date=yesterday.strftime("%d-%m-%Y"),
            to_date=today.strftime("%d-%m-%Y"),
        )
        data = data.iloc[-1]
        return jsonify(data.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})


# This returns the data of the stock for the past year. GET method is used here only for debugging and tests. POST method should be of the form:
# {"ticker": "stock ticker"}
# The response is of the form:
# [
#   {
#     "x":<float>,
#     "y":<float>
#   },
#   .
#   .
#   .
# ]
# x is the unix timestamp in milliseconds and y is the closing price.

@app.route("/api/stock/data/", methods=["POST", "GET"])
def stockData():
    if request.method == "POST":
        comp = request.get_json()
        comp = comp["ticker"].upper()
    else:
        comp = "FOCUS"
    try:
        data = capital_market.price_volume_and_deliverable_position_data(
            symbol=comp, period="1Y"
        )
        data = data[["Date", "ClosePrice"]]

        # convert date to unix timestamp
        data["Date"] = data["Date"].apply(
            lambda x: time.mktime(datetime.datetime.strptime(x, "%d-%b-%Y").timetuple())
        )
        # multiply by 1000 to convert to milliseconds for javascript
        data["Date"] = data["Date"].apply(lambda x: x * 1000)

        # Renaming for highcharts.
        data = data.rename(columns={"Date": "x", "ClosePrice": "y"})

        # FIltering out all "," and converting.
        data["y"] = data["y"].astype(str)
        data["y"] = data["y"].str.replace(",", "")
        data["y"] = data["y"].astype(float)
        return jsonify(data.to_dict(orient="records"))
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)})


# This is where we can add the model integration. Just make it in the standard python format. Formats for GET and POST are not defined and should be done so before integration.
@app.route("/model/", methods=["POST", "GET"])
def model():
    return jsonify({"data": "Model has been called! Hello from python"})


# This launches the flask server.
if __name__ == "__main__":
    # debug=True is used during development. It auto restarts the server when this file is modified.
    # app.run(debug=True)
    app.run(port=5000)


# Whenever this is deployed completly, refer to https://flask.palletsprojects.com/en/2.3.x/deploying/ for deployment.