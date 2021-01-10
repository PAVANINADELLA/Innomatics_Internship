from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def PORTFOLIO():
    return render_template('PORTFOLIO.html')

if(__name__ == '__main__'):
    app.run(debug = True)
