from base64 import b64encode
import os
from flask import (
    Flask,
    jsonify,
    redirect,
    render_template,
    request,
)
from flask_cors import CORS
import requests

ALLOWED_EXTENSIONS = {"jpeg", "jpg", "png", "pdf"}

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = os.environ.get("DEBUG", True)
_ = CORS(app)


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save():
    data = request.get_json();
    print(data)
    return jsonify({"status": "success"})

# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     if request.method != "POST":
#         return jsonify({"error": "Invalid request method"})

#     if ("file" and "image") not in request.files:
#         print("==== NO FILE PART ====")
#         return jsonify({"error": "No file part"})

#     file = request.files["image"]
#     if file.filename == "":
#         print("==== NO SELECTED FILE ====")
#         return redirect(request.url)

#     if file and allowed_file(file.filename):
#         print("==== FILE SAVED ====")
#         _ = requests.post(
#             "http://127.0.0.1:5001/draw",
#             files={"image": file.stream.read()},
#         )

#     return redirect("/draw")


# @app.route("/draw", methods=["POST", "GET"])
# def draw():
#     img_req = None
#     if request.method == "POST":
#         img_req = request.files["image"]

#     if img_req is None:
#         return """
#         <h1> No image uploaded </h1>
#         <a href="/">Go back</a>
#         """

#     return render_template(
#         "draw.html",
#         mimetype="image/jpeg",
#         image=b64encode(img_req.stream.read()).decode("ascii"),
#     )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
