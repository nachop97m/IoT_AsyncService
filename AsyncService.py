from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('New Metadata')
def handle_new_metadata_reception(data):
    print('\nData received from device:' + str(data))


if __name__ == '__main__':
    socketio.run(app)
