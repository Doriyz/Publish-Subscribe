'''
@File    :   client.py
@Time    :   2022/10/20 16:57:46
@Author  :   Zhang Maysion 
@Version :   1.0
@Contact :   zhangmx67@mail2.sysu.edu.cn
'''

import datetime
import grpc
import ps_pb2_grpc as pb2_grpc
import ps_pb2 as pb2

FORMAT = 'utf-8'


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = pb2_grpc.psStub(channel)
        while True:
            print()
            print('[HELP] Enter operation: pub, sub or exit.')
            operation = input("[INPUT] ")
            if operation == "pub":
                print('[HELP] Enter topic and content.')
                topic = input("[TOPIC] ")
                # topic = bytes(topic, FORMAT)
                content = input("[CONTENT] ")
                # content = bytes(content, FORMAT)
                requestMessage = pb2.PublishRequest()
                requestMessage.topic = topic
                requestMessage.content = content
                response = client.publish(requestMessage)
                if response.success == 1:
                    print('[PUBLISH] Publish success.')
            elif operation == "sub":
                print('[HELP] Enter topic.')
                topic = input("[TOPIC] ")
                requestMessage = pb2.SubscribeRequest(topic=topic)
                response = client.subscribe(requestMessage)
                if response.success == 1:
                    print('[SUBSCRIBE] Subscribe success.')
                    print(f'[CONTENT] {response.content}')
                else:
                    print('[ERROR] No such topic')
            elif operation == "exit":
                print('[EXIT] Byebye ~')
                break
            else:
                print("[ERROR] Invalid operation")
        

if __name__ == '__main__':
    run()