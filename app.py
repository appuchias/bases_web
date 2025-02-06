from flask import Flask, request, render_template

TEMPLATE_DIR = "templates"
STATIC_DIR = "static"

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.url_map.strict_slashes = False


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/index")
def index():
    return render_template("index.html")


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
