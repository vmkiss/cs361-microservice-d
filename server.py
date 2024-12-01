import zmq
import time
import random

def get_indices(length):
    indices = []
    for _ in range(length):
        pass
    return indices

# Establish socket connection
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

while True:
    message = socket.recv_string()
    time.sleep(1)

    result = ''

    if message:
        if message.lower() == 'q':
            context.destroy()
            break
        else:
            data = message.split('\n')
            length = data[0]
            data = data[1:]

            rand_indices = get_indices(length)

        socket.send_string(result)