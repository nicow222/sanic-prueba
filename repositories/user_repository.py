from models.user import *
from sanic import response
from config.database import get_database

async def create_user(user):
    validate = user.validate()
    
    if validate:
        return response.json({'error': validate}, status=400)
    
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]
    
    existing_user = user_collection.find_one({"email": user.email})
    if existing_user:
        return response.json({'error':"El correo electrónico ya está en uso"}, status=400)
    
    user_dict = user.to_dict()
    user_id = user_collection.insert_one(user_dict).inserted_id
    user_dict['_id'] = str(user_id)
    return User.from_dict(user_dict)


async def read_users():
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]
    
    user_collection = db["users"]
    users = user_collection.find()
    return [User.from_dict(user) for user in users]


async def read_user(user_id):
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]

    user_collection = db["users"]
    user = user_collection.find_one({'_id': user_id})
    if user:
        return User.from_dict(user)
    else:
        return None
    
async def read_user_email(email):
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]

    user_collection = db["users"]
    user = user_collection.find_one({'email': str(email)})
    if user:
        return User.from_dict(user)
    else:
        return None


async def update_user(user_id, user):
    user_dict = user.to_dict()
    dict_partial_update = {"$set": {key: value for key, value in user_dict.items() if value is not None and key in {'email', 'password', 'name'}}}
    
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]

    user_collection = db["users"]
    result = user_collection.update_one({'_id': user_id}, dict_partial_update)
    if result.modified_count == 1:
        updated_user = user_collection.find_one({'_id': user_id})
        return User.from_dict(updated_user)
    else:
        return None


async def delete_user(user_id):

    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    user_collection = db["users"]

    user_collection = db["users"]

    result = user_collection.delete_one({'_id': user_id})
    if result.deleted_count == 1:
        return True
    else:
        return False