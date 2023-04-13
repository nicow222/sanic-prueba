from repositories.mongo_repository import create_monguito 
from models.monguito import Monguito


def create_new_monguito(name):
    new_monguito = Monguito(name)
    return create_monguito(new_monguito)