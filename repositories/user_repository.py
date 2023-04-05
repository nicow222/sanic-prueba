from models.user import *
from sanic import response
from config.database import db

user_collection = db["users"]

def create_user(user):
    validate = user.validate()
    
    if validate:
        return response.json({'error': validate}, status=400)
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        return response.json({'error':"El correo electrónico ya está en uso"}, status=400)
    
    user_dict = user.to_dict()
    user_id = user_collection.insert_one(user_dict).inserted_id
    user_dict['_id'] = str(user_id)
    return User.from_dict(user_dict)


def read_users():
    users = user_collection.find()
    return [User.from_dict(user) for user in users]


def read_user(user_id):
    user = user_collection.find_one({'_id': user_id})
    if user:
        return User.from_dict(user)
    else:
        return None
    
def read_user_email(email):
    user = user_collection.find_one({'email': str(email)})
    if user:
        return User.from_dict(user)
    else:
        return None


def update_user(user_id, user):
    user_dict = user.to_dict()
    dict_partial_update = {"$set": {key: value for key, value in user_dict.items() if value is not None and key in {'email', 'password', 'name'}}}
    result = user_collection.update_one({'_id': user_id}, dict_partial_update)
    if result.modified_count == 1:
        updated_user = user_collection.find_one({'_id': user_id})
        return User.from_dict(updated_user)
    else:
        return None


def delete_user(user_id):
    result = user_collection.delete_one({'_id': user_id})
    if result.deleted_count == 1:
        return True
    else:
        return False