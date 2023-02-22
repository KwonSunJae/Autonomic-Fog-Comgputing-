import socketio
import time
import sys
sio = socketio.Client()


@sio.on('message')
def handle_message(data):
    print('Received message:', data)

@sio.event
def connect():
    print("connected")
@sio.on('connect', namespace='/socket')
def on_connect():
    print("I'm connected to the /chat namespace!")
@sio.event
def connect_error(e):
    print(e)

sio.connect('http://api-mongy.bibim-bap.com/socket')
sio.emit('connection' )
while True:
    time.sleep(1)
    print("send")
    sio.emit("log", "1 2",namespace='/socket')

sio.wait()