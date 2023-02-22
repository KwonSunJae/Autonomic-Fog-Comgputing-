import socketio
import time

sio = socketio.Client()
sio.connect()

while True:
    time.sleep(1)
    sio.emit('my message', {'foo': 'bar'})
