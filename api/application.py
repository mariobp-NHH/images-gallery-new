import os
from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
from flask_cors import CORS
from mongo_client import mongo_client

""" Define the database """
gallery = mongo_client.gallery
images_collection = gallery.images

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL="https://api.unsplash.com/photos/random"
UNSPLASH_KEY=os.environ.get("UNSPLASH_KEY", "")
DEBUG=bool(os.environ.get("DEBUG", True))
print(DEBUG)

if not UNSPLASH_KEY:
  raise EnvironmentError("Please....")


application = Flask(__name__)
application.config["DEBUG"]= DEBUG
CORS(application)


@application.route('/')
def home():
  return "<h1>Welcome Home, Mario!</h1>"

@application.route('/new-image')
def new_image():
  word = request.args.get("query")
  headers= {
    "Accept-Version": "v1",
    "Authorization": "Client-ID " + UNSPLASH_KEY
  }
  params = {
    "query": word
  }
  response = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
  print(response.text)
  data = response.json()
  return data 

@application.route("/images", methods=["GET","POST"])
def images():
  if request.method == "GET":
    images = images_collection.find({})
    return jsonify([img for img in images])
  if request.method == "POST":
    image = request.get_json()
    image["_id"] = image.get("id")
    result = images_collection.insert_one(image)
    inserted_id = result.inserted_id
    return {"inserted_id": inserted_id}
  
@application.route("/images/<image_id>", methods=["DELETE"])
def image(image_id):
  if request.method == "DELETE":
    result = images_collection.delete_one({"_id": image_id})
    print(result)
    return {"deleted_id": image_id}

if __name__=='__main__':
  application.run(host="0.0.0.0", port=5000)  