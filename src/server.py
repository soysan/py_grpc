from concurrent import futures
import grpc
from pb.helloworld_pb2_grpc import HelloWorldServiceServicer, add_HelloWorldServiceServicer_to_server
from pb.helloworld_pb2 import HelloWorldRes

class Greeter(HelloWorldServiceServicer):

    def SayHello(self, request, context):
        return HelloWorldRes(message='Hello, world!')

    def Bye(self, request, context):
        return HelloWorldRes(message='Bye!')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_HelloWorldServiceServicer_to_server(Greeter(), server)

    server.add_insecure_port('[::]:5051')
    server.start()

    print('Server started at port 5051')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
