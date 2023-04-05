from sanic_jwt import exceptions
from config.database import db
from models.user import User

user_collection = db["users"]

async def authenticate(request, *args, **kwargs):
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if not email or not password:
        raise exceptions.AuthenticationFailed("Missing username or password.")
    
    user_dict = user_collection.find_one({"email": email})
    if user_dict is None:
        raise exceptions.AuthenticationFailed("User not found.")

    user = User.from_dict(user_dict)
    if password != user.password:
        raise exceptions.AuthenticationFailed("Password is incorrect.")

    return user
