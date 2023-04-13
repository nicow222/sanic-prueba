from models.monguito import *
from sanic import response
from config.database import get_database


async def create_monguito(monguito):
    validate = monguito.validate()
    
    if validate:
        return response.json({'error': validate}, status=400)
    
    db = await get_database()        
    if db is None:
        raise Exception("Fallo al establecer conexion con la BD")
    monguito_collection = db["monguito"]

    monguito_collection.create_index("name", unique=True)
    
    monguito_dict = monguito.to_dict()
    monguito_id = monguito_collection.insert_one(monguito_dict).inserted_id
    monguito_dict['_id'] = str(monguito_id)
    return Monguito.from_dict(monguito_dict)