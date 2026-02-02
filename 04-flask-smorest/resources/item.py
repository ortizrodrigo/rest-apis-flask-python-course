import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores, items

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
  def get(self, item_id):
    try:
      return items[item_id]
    except KeyError:
      abort(404, message="Item not found.")

  def put(self, item_id):
    item_data = request.get_json()

    required_keys = ["price", "name"]
    missing_keys = [k for k in required_keys if k not in item_data]
    if missing_keys:
      abort(400, message=f"Missing required keys: {', '.join(missing_keys)}")

    try:
      item = items[item_id]
      item |= item_data
      return item
    except KeyError:
      abort(404, message="Item not found.")

  def delete(self, item_id):
    try:
      del items[item_id]
      return {"message": "Item deleted."}
    except KeyError:
      abort(404, message="Item not found.")

@blp.route("/item")
class ItemList(MethodView):
  def get(self):
    return {"items": list(items.values())}

  def post(self):
    item_data = request.get_json()

    required_keys = ["price", "store_id", "name"]
    missing_keys = [k for k in required_keys if k not in item_data]
    if missing_keys:
      abort(400, message=f"Missing required keys: {', '.join(missing_keys)}")

    for item in items.values():
      if item_data["name"] == item["name"] and item_data["store_id"] == item["store_id"]:
        abort(400, message=f"Item already exists.")

    if item_data["store_id"] not in stores:
      abort(404, message="Store not found.")
    
    item_id = uuid.uuid4().hex
    item = {**item_data, "id": item_id}
    items[item_id] = item

    return item, 201