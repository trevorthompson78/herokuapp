from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alcohol')
def alcohol():
    return render_template('alcohol.html')

@app.route('/legends')
def legends():
    return render_template('legends.html')

@app.route('/arrowheads')
def arrowheads():
    return render_template('arrowheads.html')

@app.route('/farmland')
def farmland():
    return render_template('farmanimals.html')

@app.route('/forrest_river')
def forrest_river():
    return render_template('forrest_river.html')

@app.route('/heirlooms')
def heirlooms():
    return render_template('heirlooms.html')

@app.route('/mountain_grassland')
def mountain_grassland():
    return render_template('mountain_grassland.html')

@app.route('/wetland')
def wetland():
    return render_template('wetland.html')

@app.route('/desert')
def desert():
    return render_template('desert.html')

@app.route('/bird_eggs')
def bird_eggs():
    return render_template('bird_eggs.html')

@app.route('/bracelets')
def bracelets():
    return render_template('bracelets.html')

@app.route('/coins')
def coins():
    return render_template('coins.html')

@app.route('/suitofcups')
def suitofcups():
    return render_template('suitofcups.html')

@app.route('/suitofpentacles.html')
def suitofpentacles():
    return render_template('pentacles.html')

@app.route('/suitofswords.html')
def suitofswords():
    return render_template('suitofswords.html')

@app.route('/suitofwands.html')
def suitofwands():
    return render_template('suitofwands.html')

@app.route('/wildflowers')
def wildflowers():
    return render_template('wildflowers.html')

@app.route('/necklaces')
def necklaces():
    return render_template('necklaces.html')

@app.route('/rings')
def rings():
    return render_template('rings.html')

@app.route('/earings')
def earings():
    return render_template('earings.html')

@app.route('/herbs')
def herbs():
    return render_template('herbs.html')

if __name__ == '__main__':
    app.run(debug = True)