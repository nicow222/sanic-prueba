from sanic import Blueprint, response
from services.mongo_service import create_new_monguito
from sanic_jwt.decorators import protected
from config.rabbitmq import publish_rabbitmq

monguito_routes = Blueprint('monguito', url_prefix='/monguito/')


@monguito_routes.route('/error/', methods=['POST'])
async def create_monguito(request):
    monguito = request.json if request.json else {}
    created_monguito = await create_new_monguito(monguito.get('name'))
    if isinstance(created_monguito,response.JSONResponse):
        return created_monguito    
    monguito_dicc = created_monguito.to_dict()
    # Publicar un mensaje en la cola de RabbitMQ con el ID del usuario recién creado
    #await publish_rabbitmq('monguito_queue',monguito_dicc['_id'])
    return response.json(monguito_dicc, status=201)