from sanic import Blueprint, response
from services.server_grpc import print_message

grpc_routes = Blueprint('grpc', url_prefix='/grpc/')

@grpc_routes.route('/', methods=['GET'])
async def print_message_route(request):
    resp = {'message': print_message()}
    return response.json(resp)