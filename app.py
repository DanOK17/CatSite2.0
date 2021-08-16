from flask import Flask, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:admin@cluster0.x09us.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client.Cluster0
images = db["images"]

@app.route("/cats/<int:image_id>")
def index(image_id):
    result = images.find_one({"_id": image_id})["title"]
    return render_template("index.html", url=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
