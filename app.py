from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return "flask cd program for testing jenkins pipeline 14"

@app.route('/new')
def index():
    return "new feature added for testing jenkins pipeline"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)