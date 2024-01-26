#!/bin/bash

build () {
    echo "Building..."
    sudo docker build -t grpc .
}

start () {
    echo "Starting..."
    sudo docker run -itd --rm --name grpc -v $(pwd):/app grpc
}

stop () {
    echo "Stopping..."
    docker stop grpc
}

proto () {
    echo "Generating proto..."
    docker exec grpc python3 -m grpc_tools.protoc -I./src/proto --python_out=./src/pb --pyi_out=./src/pb --grpc_python_out=./src/pb ./src/proto/helloworld.proto
}

if [ "$1" == "build" ]; then
    build
elif [ "$1" == "start" ]; then
    start
elif [ "$1" == "stop" ]; then
    stop
elif [ "$1" == "proto" ]; then
    proto
else
    echo "Usage: ./run.sh [build|start|stop|proto]"
fi