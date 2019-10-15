from flask import Flask, render_template
from flask_socketio import SocketIO
from data import Data
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

recv = Data()

@socketio.on('New Metadata')
def handle_new_metadata_reception(data):
    recv.received(json.dumps(data))
    recv.show()



if __name__ == '__main__':
    socketio.run(app)
