from flask import Flask, render_template, request, session, redirect, url_for
from nselib import capital_market
import pandas
#!TODO - add session to store ticker
#!TODO - add functionality to stocks page: getting reddit data and twitter data and the graph thingy.


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'ticker' not in session:
        session['ticker'] = "default"
    return render_template('home.html', comp = session['ticker'])

@app.route('/stocks', methods = ['GET', 'POST'])
def stocks():
    if request.method == 'POST':
        print("SAD")
        session['ticker'] = request.form['ticker']
        data = capital_market.price_volume_and_deliverable_position_data(symbol=session['ticker'], from_date='06-06-2023', to_date='06-07-2023')
        print(data)
        return render_template('stocks.html', ticker=session['ticker'], req_type = request.method, column_names=data.columns.values, row_data=list(data.values.tolist()), zip=zip)
    else:
        return render_template('stocks.html', req_type = request.method)

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    #checking if it is a post or get method
    if request.method == 'POST':
        return render_template('formtest.html', req_type = request.method, form_data = request.form)
    else:
        return render_template('formtest.html', req_type = request.method)

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)