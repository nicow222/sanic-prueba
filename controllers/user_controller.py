from sanic import Blueprint, response
from services.user_service import (create_new_user, get_all_users, get_user_by_email,
                                    get_user_by_id, update_user_by_id, delete_user_by_id)
from sanic_jwt.decorators import protected
from config.rabbitmq import publish_rabbitmq

user_routes = Blueprint('user', url_prefix='/users/')


@user_routes.route('/', methods=['GET'])
@protected()
async def get_users(request):
    users = await get_all_users()
    return response.json([user.to_dict() for user in users])


@user_routes.route('/<user_id>', methods=['GET'])

async def get_user(request, user_id):
    user = get_user_by_id(user_id)
    if user:
        return response.json(user.to_dict())
    else:
        return response.text('User not found', status=404)


@user_routes.route('/obtener/', methods=['POST'])
@protected()
async def get_user_email(request):
    user = await get_user_by_email(request.json.get('email',None))
    if user:
        return response.json(user.to_dict())
    else:
        return response.text('User not found', status=404)


@user_routes.route('/', methods=['POST'])

async def create_user(request):
    user = request.json
    created_user = await create_new_user(user.get('email'), user.get('password'), user.get('name'))
    if isinstance(created_user,response.JSONResponse):
        return created_user    
    user_dicc = created_user.to_dict()
    # Publicar un mensaje en la cola de RabbitMQ con el ID del usuario recién creado
    await publish_rabbitmq('users_queue',user_dicc['_id'])
    return response.json(user_dicc, status=201)


@user_routes.route('/<user_id>/', methods=['PUT'])
@protected()
async def update_user(request, user_id):
    user = request.json
    updated_user = await update_user_by_id(user_id, user.get('name'), user.get('email'), user.get('password'))
    if updated_user:
        return response.json(updated_user.to_dict())
    else:
        return response.text('User not found', status=404)


@user_routes.route('/<user_id>/', methods=['DELETE'])
@protected()
async def delete_user(request, user_id):
    deleted = await delete_user_by_id(user_id)
    if deleted:
        return response.text('User deleted', status=204)
    else:
        return response.text('User not found', status=404)