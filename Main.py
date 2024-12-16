# app.py

from flask import Flask, render_template, request
import helper

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'Welt')  # Optionaler Parameter 'name' aus der URL
    greeting = helper.greet_user(name)  # Nutzung der Funktion aus helper.py
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
