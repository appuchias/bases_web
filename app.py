from flask import Flask, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello, {name}!"


@app.route("/hello")
def hello():
    # Parámetro de una petición GET
    name = request.args.get("name", "")

    if name:
        return f"Hello, {name}!"

    return "No name provided"


@app.route("/post", methods=["POST"])
def post():  # Content-Type: application/x-www-form-urlencoded
    args = request.form
    if args:
        return f"You made a POST request with args: {args}"

    return "You made a POST request without args"
