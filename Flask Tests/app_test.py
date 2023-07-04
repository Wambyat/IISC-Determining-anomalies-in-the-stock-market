from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    #checking if it is a post or get method
    if request.method == 'POST':
        return render_template('formtest.html', req_type = request.method, form_data = request.form)
    else:
        return render_template('formtest.html', req_type = request.method)

if __name__ == '__main__':
    app.run(debug=True)