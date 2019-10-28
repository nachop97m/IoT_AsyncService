import pytest
import json
from src.data import Data
import socketio
import requests
import time


class TestData:

    data = {
        'device': '1',
        'seqNumber': 0,
        'data': {
            'temperature': 10,
            'latitude': 38,
            'longitude': 20
            },
        'time': '2019-10-10 17:00:00'
        }

    dataR = Data()

    def test_received(self):

        rec = self.dataR.received(json.dumps(self.data))
        assert self.data.get('device') == rec.get('device')
        assert self.data.get('seqNumber') == rec.get('seqNumber')
        assert self.data.get('data').get('temperature') == rec.get('data').get('temperature')

    def test_get_data(self):

        rec = self.dataR.received(json.dumps(self.data))
        getted = self.dataR.get_data()
        assert getted.get('device') == rec.get('device')
        assert getted.get('seqNumber') == rec.get('seqNumber')
        assert getted.get('data').get('temperature') == rec.get('data').get('temperature')


class TestService:

    device = {
        'device': '5',
        'seqNumber': 0,
        'data': {
            'temperature': 11.650820695464724,
            'latitude': 37.19882735156563,
            'longitude': -3.6204751311128334
            },
        'time': '2019-10-27 21:27:58.899064'
        }

    def test_reception(self):

        # api-endpoint
        URL = "http://localhost:5000/last_received"

        sio = socketio.Client()
        sio.connect('http://localhost:5000')
        sio.emit('New Metadata', self.device)

        time.sleep(3)

        sio.disconnect()

        r = requests.get(URL)
        data = r.json()

        assert data.get('device') == self.device.get('device')
        assert data.get('data').get('latitude') == self.device.get('data').get('latitude')
        assert data.get('data').get('longitude') == self.device.get('data').get('longitude')
