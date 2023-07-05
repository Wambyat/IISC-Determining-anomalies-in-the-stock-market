from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    session['ticker'] = "AAPL"
    return render_template('home.html', comp = session['ticker'])

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    #checking if it is a post or get method
    if request.method == 'POST':
        return render_template('formtest.html', req_type = request.method, form_data = request.form)
    else:
        return render_template('formtest.html', req_type = request.method)

@app.route('/login')
def login():
    return "Thid is the login page"

# Error Handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)