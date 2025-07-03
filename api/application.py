import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
from flask_cors import CORS


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

if __name__=='__main__':
  application.run(host="0.0.0.0", port=5000)  