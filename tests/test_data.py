import pytest
import json
from src.data import Data


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
        assert self.data.get('data').get('temperature') ==
        rec.get('data').get('temperature')

    def test_get_data(self):

        rec = self.dataR.received(json.dumps(self.data))
        getted = self.dataR.get_data()
        assert getted.get('device') == rec.get('device')
        assert getted.get('seqNumber') == rec.get('seqNumber')
        assert getted.get('data').get('temperature') ==
        rec.get('data').get('temperature')
