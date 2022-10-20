'''
@File    :   server.py
@Time    :   2022/10/20 16:57:32
@Author  :   Zhang Maysion 
@Version :   1.0
@Contact :   zhangmx67@mail2.sysu.edu.cn
'''

import json
import grpc
from concurrent import futures
import datetime
import ps_pb2_grpc as pb2_grpc
import ps_pb2 as pb2

# use a dictionary to store the messages
# the key is the topic and the value is content


# def getTimestamp():
#     dt = datetime.datetime.now()
#     return pb2.timestamp(year = dt.year, month = dt.month, day = dt.day, hour = dt.hour, minute = dt.minute, second = dt.second)



class psService(pb2_grpc.psServicer):
    
    message_dict = {} 
    time_dict = {}

    def __init__(self, message_dict, time_dict, **kwargs):
        self.message_dict = message_dict
        self.time_dict = time_dict

    def publish(self, request, content):
        """
        publish a message to a topic
        """
        # before publish, delete the out-time message
        # using a list comprehension to make a list of the keys to be deleted
        delete = []
        for key in self.time_dict:
            time = self.time_dict[key]
            dt = datetime.datetime.strptime(time[0:26], "%Y-%m-%d %H:%M:%S") 
            if dt + datetime.timedelta(seconds=60) < datetime.datetime.now():
                delete.append(key)
        for key in delete:
            print(f'[DELETE] Delete topic {key}')
            self.message_dict.pop(key)
            self.time_dict.pop(key)
        if len(request.content) != 0:
            print(f'[PUBLISH] Add topic {request.topic}')
            self.message_dict[request.topic] = request.content
            # it does not work to store datetime to a json file
            self.time_dict[request.topic] = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
            # write the message to a locol file to restore
            with open('message.json', 'w') as json_file:
                json.dump(self.message_dict, json_file)
            with open('time.json', 'w') as json_file:
                json.dump(self.time_dict, json_file)
            return pb2.PublishResponse(success = 1) 
        else:
            return pb2.publishResponse(success = 0)


    def subscribe(self, request, content):
        """
        subscribe a topic and get the message
        """
        while True:
            if request.topic in self.message_dict:
                print(f'[SUBSCRIBE] Subscribe topic {request.topic}')
                return pb2.SubscribeResponse(success = 1 , content = self.message_dict[request.topic])
            else:
                return pb2.SubscribeResponse(success = 0, content = '')


def serve():
    print('[START] Server is working now.')
    # firsly load the message dictionary
    json_file = open('message.json', 'r')
    message_dict = json.load(json_file)
    json_file.close()
    
    json_file = open('time.json', 'r')
    time_dict = json.load(json_file)
    json_file.close()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_psServicer_to_server(psService(message_dict, time_dict ), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()