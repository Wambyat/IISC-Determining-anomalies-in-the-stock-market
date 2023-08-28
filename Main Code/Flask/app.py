from flask import Flask, jsonify, request
from flask_cors import CORS
from nselib import capital_market
import datetime

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


# This is just a testing route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello World!"})


# This is just a testing route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


# This finds the stock in the list of stocks and returns the ticker and name. If not found, returns Invalid ticker
@app.route("/api/search", methods=["POST"])
def search():
    try:
        data = request.get_json()
        input = data["search"].upper()
        data = capital_market.equity_list()
        data = data[["SYMBOL", "NAME OF COMPANY"]]
        test = {data["SYMBOL"][i]: data["NAME OF COMPANY"][i] for i in range(len(data))}
        try:
            return jsonify({"name": test[input], "ticker": input})
        except KeyError:
            return jsonify({"error": "Invalid ticker <only nse is supported>"})
    except Exception as e:
        return jsonify({"error": str(e)})


# This returns the list of all the stocks in the NSE
@app.route("/api/all", methods=["GET"])
def all():
    try:
        data = capital_market.equity_list()
        data = data[["SYMBOL", "NAME OF COMPANY"]]
        test = {data["SYMBOL"][i]: data["NAME OF COMPANY"][i] for i in range(len(data))}
        return jsonify(test)
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/api/stock/", methods=["POST", "GET"])
def stock():
    if request.method == "POST":
        comp = request.get_json()
        comp = comp["ticker"].upper()
    else:
        comp = "FOCUS"
    try:
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


@app.route("/model/", methods=["POST", "GET"])
def model():
    return jsonify({"data":"Model has been called! Hello from python"})


if __name__ == "__main__":
    app.run(debug=True)
