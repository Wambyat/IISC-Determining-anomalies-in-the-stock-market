from flask import Flask, render_template, request, session, redirect, url_for
from nselib import capital_market
import pandas as pd
import praw

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
        #!TODO take ticker and get company name
        #this is creating a reddit praw thingy and getting the data based on ticker
        user_agent = "praw_scraper_1.0"
        reddit = praw.Reddit(
                            username=request.form['username'],
                            password=request.form['passw'],
                            client_id="vKxcl2gZOIFpwXw52cJr-A",
                            client_secret="iOAq0BDKtBapF5Lf-S_z4_Ckj_tDvQ",
                            user_agent=user_agent
        )
        subreddit_name = "all"
        subreddit = reddit.subreddit(subreddit_name)
        comp = session['ticker']
        data = capital_market.equity_list()
        b = data.loc[data['SYMBOL']==comp]['NAME OF COMPANY']
        try:
            inp = b.values[0]
        except IndexError:
            t = session['ticker']
            session['ticker'] = "default"
            return render_template('badstocks.html', ticker=t)
        results=subreddit.search(inp, limit=10)

        data = pd.DataFrame()
        titles=[]
        scores=[]
        ids=[]

        # Looping thru the result to get the title, score and id of the post
        # subreddit can have a few different params: top, new, hot etc.
        for res in results:    
            titles.append(res.title)
            scores.append(res.score) #upvotes
            ids.append(res.id)

        data['Title'] = titles
        data['Id'] = ids
        data['Upvotes'] = scores

        # data = capital_market.price_volume_and_deliverable_position_data(symbol=session['ticker'], from_date='06-06-2023', to_date='06-07-2023')
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