from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'this is auto-deployed via Google Cloud API'

@app.route('/name/<value>')
def name(value):
    print(f"You passed in this variable into the url: {value}")
    val = {"value": value}
    return jsonify(val)

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
