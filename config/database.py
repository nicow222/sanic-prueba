from pymongo import MongoClient

db = None

async def get_database():
    global db
   
    if db is not None:
        return db

    try:
        # Create a new database connection
        client = MongoClient("mongodb://localhost:27017/")
        db = client["sanic"]
    except Exception as e:
        print(f"Fallo al establecer conexion con la BD: {e}")
        db = None

    return db
