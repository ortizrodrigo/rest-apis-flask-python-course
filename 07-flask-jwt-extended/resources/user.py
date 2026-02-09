from flask.views import MethodView
from flask_smorest import Blueprint, abort
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import UserModel
from schemas import UserSchema

blp = Blueprint("Users", "users", description="Operations on users") 

@blp.route("/register")
class UserRegister(MethodView):
  @blp.arguments(UserSchema)
  def post(self, user_data):
    hashed_password = pbkdf2_sha256.hash(user_data["password"])
    user = UserModel(username=user_data["username"], password=hashed_password)

    try:
      db.session.add(user)
      db.session.commit()
    except IntegrityError:
      db.session.rollback()
      abort(409, message="A user with that username already exists.")
    except SQLAlchemyError:
      db.session.rollback()
      abort(500, message="An error occurred while registering the user.")
    
    return {"message": "User created successfully."}, 201
  
@blp.route("/user/<int:user_id>")
class User(MethodView):
  @blp.response(200, UserSchema)
  def get(self, user_id):
    user = UserModel.query.get_or_404(user_id)
    return user
  
  def delete(self, user_id):
    user = UserModel.query.get_or_404(user_id)

    try:
      db.session.delete(user)
      db.session.commit()
    except SQLAlchemyError:
      db.session.rollback()
      abort(500, message="An error occurred while deleting the user.")

    return {"message": "User deleted."}, 200