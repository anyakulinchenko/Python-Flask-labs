from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world !"

@app.route("/api/v1/hello-world-12")
def hello_world():
    return "Hello World 12"

if __name__ == "__main__":
    app.run(debug=True)

