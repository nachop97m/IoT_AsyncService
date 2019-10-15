import json

class Data:

    data = json.dumps({})

    def received(self, rec):

        try:
            self.data = json.loads(rec)
        except ValueError as e:
            print ('Received value is not JSONizable')

        return self.data

    def show(self):
        print(str(self.data))

    def get_data(self):
        return self.data
