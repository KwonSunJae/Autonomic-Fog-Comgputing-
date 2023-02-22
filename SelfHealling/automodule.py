import socketio
import time
import sys
sio = socketio.Client()
sio.connect('http://api-mongy.bibim-bap.com/socket')

while True:
    time.sleep(1)
    sio.emit(sys.argv[1]+' '+sys.argv[2])
