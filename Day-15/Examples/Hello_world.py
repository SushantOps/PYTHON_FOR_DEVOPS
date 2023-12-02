from flask import Flask

## creating flask application instance
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run("0.0.0.0")
