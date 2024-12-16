from flask import Flask, render_template, request
import Helper

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name', 'Welt')
    greeting = Helper.greet_user(name)
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)

