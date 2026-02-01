from flask import Flask

app = Flask(__name__)

stores = [
  {
    "name": "My Store",
    "items": [
      {
        "name": "Chair",
        "price": 15.99
      }
    ]
  }
]

@app.route("/store", methods=["GET"]) # http://127.0.0.1:5000/store (GET)
def get_stores():
  return {"stores": stores}