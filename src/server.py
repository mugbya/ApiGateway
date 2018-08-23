from sanic import Sanic
from sanic.response import json
from src.routes.user.userApi import user_bp
from src import settings
import asyncio
from datetime import datetime
app = Sanic()


app.blueprint(user_bp)


@app.route('/')
async def test(request):
    print('[{0}] start time: {1}'.format(request.transport, datetime.now()))
    await asyncio.sleep(5)
    print('[{0}] end time: {1}'.format(request.transport, datetime.now()))
    return json({'hello': 'world'})


if __name__ == '__main__':
    app.run(host=settings.HOST, port=settings.PORT)


