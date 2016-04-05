import sys
import subprocess
from os import path
from time import sleep

import zmq

file_dir = path.dirname(__file__)
main_file = path.abspath(path.join(file_dir,
                                   '..',
                                   'languageprocessing',
                                   '__main__.py'))

text_address = 'tcp://127.0.0.1:5578'
result_address = 'tcp://127.0.0.1:5579'

subprocess_args = (sys.executable,
                   main_file,
                   '--text_address',
                   text_address,
                   '--result_address',
                   result_address)

subprocess = subprocess.Popen(subprocess_args)
context = zmq.Context()

text_socket = context.socket(zmq.PUB)
text_socket.bind(text_address)

result_socket = context.socket(zmq.SUB)
result_socket.setsockopt(zmq.SUBSCRIBE, b'')
result_socket.connect(result_address)

# give our sockets a chance to connect
sleep(1)

example_text = b'This morning is easy like Sunday Morning'
text_socket.send(example_text)

result = result_socket.recv_pyobj()
print(result)
subprocess.terminate()
