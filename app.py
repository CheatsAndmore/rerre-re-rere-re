from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/room/<name>')
def room(name):
    return render_template('room.html', name=name)

if __name__ == '__main__':
    app.run()
