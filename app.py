

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Silly Hello, World!</h1><p>This is a silly web app.</p>'

if __name__ == '__main__':
    app.run(port=5000)

