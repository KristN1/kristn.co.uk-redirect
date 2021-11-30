from waitress import serve
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

from utils import idgen, mysql
db = mysql.MySQL()

base_url = "https://kristn.tech/r"

def validate_url(url):
    if url == None:
        return jsonify({"message": "400, No url header provided"}), 400

    elif not url.startswith("http"):
        return jsonify({"message": "400, Invalid url"}), 400

    if "." not in url:
        return jsonify({"message": "400, Invalid url"}), 400

    else:
        return True

@app.route("/")
def index():
    return "kristn.tech public redirect service. Send POST to /create with a url header to create a redirect"

@app.route("/<url_id>")
def _redirect(url_id):
    redirect_url = db.get_redirect(url_id)

    if redirect_url == None:
        return jsonify({"message": "404, No such url"}), 404

    return redirect(redirect_url)

@app.route("/create", methods=["POST"])
def create():
    url = request.headers.get("url")
    url_validation = validate_url(url)

    if url_validation == True:
        redirect_id = idgen.generate()

        if db.get_redirect(redirect_id) == None:
            db.add_redirect(redirect_id, request.headers["url"])
            return jsonify({"redirect_id": redirect_id, "full_url": base_url + "/" + redirect_id})
        else:
            create()
    
    else:
        return url_validation


if __name__ == "__main__":
    port = 5000

    print(f"Serving on {port}")
    serve(app, port=port)