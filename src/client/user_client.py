from __future__ import print_function

import grpc
import settings
from src.proto.user import user_pb2
from src.proto.user import user_pb2_grpc


class UserClient(object):
    channel = grpc.insecure_channel('{0}:{1}'.format(settings.MS_USER_ADDRESS, settings.MS_USER_PORT))
    stub = user_pb2_grpc.UserApiStub(channel)

    @classmethod
    def get_client(cls):
        return cls.stub


def run():
    channel = grpc.insecure_channel('{0}:{1}'.format(settings.MS_USER_ADDRESS, settings.MS_USER_PORT))
    stub = user_pb2_grpc.UserApiStub(channel)

    add_user_req = user_pb2.AddUserReq(name="mugbya")
    response = stub.addUser(add_user_req)

    print("user client received code: {0} , message: {1}".format(response.code, response.message) )


if __name__ == '__main__':
    run()


user_client = UserClient.get_client()
