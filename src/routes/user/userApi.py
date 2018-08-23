from sanic.blueprints import Blueprint
from src.client.user_client import user_client
from src.proto.user import user_pb2
from sanic.response import file, json
user_bp = Blueprint('user', url_prefix='/user')


@user_bp.post('/add_user')
async def add_user(request):
    name = request.json.get('name', None)

    add_user_req = user_pb2.AddUserReq(name=name)
    res = user_client.addUser(add_user_req)

    print(res)

    return json({})
