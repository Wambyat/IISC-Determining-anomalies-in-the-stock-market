from flask import Flask, jsonify, request
from flask_cors import CORS
from nselib import capital_market

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello World!"})


# sanity check route
@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong!")


@app.route("/api/search", methods=["POST"])
def search():
    try:
        data = request.get_json()
        input = data["search"]
        data = capital_market.equity_list()
        b = data.loc[data["SYMBOL"] == input]["NAME OF COMPANY"]
        try:
            return jsonify({"name": b.values[0]})
        except IndexError:
            return jsonify({"error": "Invalid ticker <only nse is supported>"})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
