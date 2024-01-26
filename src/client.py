import grpc
from pb.helloworld_pb2_grpc import HelloWorldServiceStub
from pb.helloworld_pb2 import HelloWorldReq

def run():
    with grpc.insecure_channel('localhost:5051') as channel:
        stub = HelloWorldServiceStub(channel)
        response = stub.SayHello(HelloWorldReq())
        test = stub.Bye(HelloWorldReq())
    print(response.message)
    print(test.message)

if __name__ == '__main__':
    run()
