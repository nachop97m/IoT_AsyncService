from flask import Flask, render_template, redirect, url_for, make_response
from flask_socketio import SocketIO
from data import Data
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
socketio = SocketIO(app)

recv = Data()


@socketio.on('New Metadata')
def handle_new_metadata_reception(data):
    recv.received(json.dumps(data))
    recv.show()


@app.route("/")
def home():
    return redirect(url_for('lastReceived'))


@app.route("/status")
def status():
    status = {"status": "OK"}
    headers = {"Content-Type": "json"}
    return make_response(status, 200, headers)


@app.route("/last_received")
def lastReceived():
    lastRec = recv.get_data()
    headers = {"Content-Type": "json"}
    return make_response(lastRec, 200, headers)


if __name__ == '__main__':
    socketio.run(app)
