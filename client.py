'''
@File    :   client.py
@Time    :   2022/10/20 16:57:46
@Author  :   Zhang Maysion 
@Version :   1.0
@Contact :   zhangmx67@mail2.sysu.edu.cn
'''


import grpc
import ps_pb2_grpc as pb2_grpc
import ps_pb2 as pb2

FORMAT = 'utf-8'

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = pb2_grpc.psStub(channel)
        while True:
            operation = input("Enter operation: pub, sub or exit\n")
            if operation == "pub":
                topic = input("Enter topic: \n")
                # topic = bytes(topic, FORMAT)
                content = input("Enter content: \n")
                # content = bytes(content, FORMAT)
                requestMessage = pb2.PublishRequest()
                requestMessage.topic = topic
                requestMessage.content = content
                response = client.publish(requestMessage)
                print(response)
            elif operation == "sub":
                topic = input("Enter topic: \n")
                requestMessage = pb2.SubscribeRequest(topic=topic)
                response = client.subscribe(requestMessage)
                if response.success == 1:
                    print(f'the content is {response.content}')
                else:
                    print('no such topic')
            elif operation == "exit":
                break
            else:
                print("Invalid operation")
        

if __name__ == '__main__':
    run()

'''

class Client(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.psStub(self.channel)


    def subscribe(self, requestMessage):
        return self.stub.subscribe(requestMessage)

    def publish(self, requesMessage):
        return self.stub.publish(requesMessage)

if __name__ == '__main__':
    client = Client()
    while True:
        operation = input("Enter operation: pub, sub or exit\n")
        if operation == "pub":
            topic = input("Enter topic: \n").encode(FORMAT)
            content = input("Enter content: \n").encode(FORMAT)
            requestMessage = pb2.PublishRequest(topic=topic, content=content)
            response = client.publish(requestMessage)
            print(response)
        elif operation == "sub":
            topic = input("Enter topic: \n")
            requestMessage = pb2.SubscribeRequest(topic=topic)
            response = client.subscribe(requestMessage)
            print(response)
        elif operation == "exit":
            break
        else:
            print("Invalid operation")
    

    '''