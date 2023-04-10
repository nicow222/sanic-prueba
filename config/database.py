from pymongo import MongoClient
import os

db = None
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
async def get_database():
    global db
   
    if db is not None:
        return db

    try:
        # Create a new database connection
        client = MongoClient(f'mongodb://{mongo_host}:27017/')
        db = client["sanic"]
    except Exception as e:
        print(f"Fallo al establecer conexion con la BD: {e}")
        db = None

    return db
