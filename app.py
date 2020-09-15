from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/alcohol')
def alcohol():
    return render_template('alcohol.html')

@app.route('/legends')
def legends():
    return render_template('legends.html')

if __name__ == '__main__':
    app.run(debug = True)