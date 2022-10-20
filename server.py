'''
@File    :   server.py
@Time    :   2022/10/20 16:57:32
@Author  :   Zhang Maysion 
@Version :   1.0
@Contact :   zhangmx67@mail2.sysu.edu.cn
'''


import grpc
from concurrent import futures
import datetime
import ps_pb2_grpc as pb2_grpc
import ps_pb2 as pb2

# use a dictionary to store the messages
# the key is the topic and the value is content
message_dict = {} 

class psService(pb2_grpc.psServicer):

    def __init__(self, *args, **kwargs):
        pass

    def publish(self, request, content):
        """
        publish a message to a topic
        """
        if len(request.content) != 0:
            print(f'[PUBLISH] Add topic {request.topic}')
            message_dict[request.topic] = request.content
            return pb2.PublishResponse(success = 1) 
        else:
            return pb2.publishResponse(success = 0)


    def subscribe(self, request, content):
        """
        subscribe a topic and get the message
        """
        print(f'[SUBSCRIBE] Subscribe topic {request.topic}')
        while True:
            if request.topic in message_dict:
                return pb2.SubscribeResponse(success = 1 , content = message_dict[request.topic])
            else:
                return pb2.SubscribeResponse(success = 0, content = '')

'''     
class UnaryService(pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):

        # get the string from the incoming request
        message1 = request.message1
        message2 = request.message2
        result = f'{message1}  {message2}'
        result = {'message': result, 'received': True}

        return pb2.MessageResponse(**result)

'''

def serve():
    print('[START] Server is working now.')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_psServicer_to_server(psService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()