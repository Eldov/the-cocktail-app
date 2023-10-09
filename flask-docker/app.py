# Imports
import requests
import pandas as pd
from cocktail_app import getDrink
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    df = None
    drink_name = None
    if request.method == 'POST':
        try:
            drink_name = request.form.get('drink', type=str)
            df = getDrink(drink_name)
        except:
            return render_template('exception.html')

    return render_template('index.html', tables=[df.to_html(classes='data', header="true")] if df is not None else None)

if __name__ == "__main__":
    app.run(debug=True)