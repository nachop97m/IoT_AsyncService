import geopy.distance
import time
import os
import socketio

from datetime import datetime
from random import random, randint, uniform
from argparse import ArgumentParser

#Initial temp value
TEMP = uniform(-20,20)


#Initial coordinates (ETSIIT)
LATITUDE = 37.19672790095874
LONGITUDE = -3.6244958639144897

PT =[LATITUDE, LONGITUDE]

sio = socketio.Client()

sio.connect('http://localhost:5000')

def get_nearby_point(origin = PT, km_distance=0.1, radius=180):
    """
    Gets a nearby point, based on an origin, a distance and a direction.

    :param origin: {tuple} Origin point in format (lat, long)
    :param km_distance: {float} Distance in kms for the next point
    :param radius: {int} Direction of the new point, in degrees [0, 360]
    :return: New tuple with the (lat, long) for a new point
    """
    dist = geopy.distance.VincentyDistance(kilometers=km_distance)
    pt = dist.destination(point=geopy.Point(origin), bearing=random()*radius)

    return pt[0], pt[1]


def generateTemp():
    """
    Function to generate a random temp value
    :return:int Random temp value
    """

    global TEMP

    aux = TEMP
    TEMP = TEMP + uniform(-5, 5)

    while TEMP < -50 or TEMP > 50:
        TEMP = aux
        TEMP = TEMP + uniform(-5, 5)

    return TEMP


def sendData(data):

    """
    Function to send Device Metadata by socketIO socket
    :param data: json with the data to send
    :return: nothing
    """
    try:

        sio.emit('New Metadata', data)

    except:

        print ('Failed when trying to send data')


if __name__ == "__main__":



    argp = ArgumentParser(description = "Device data generator")

    argp.add_argument('-n', '--number', help = 'Device id identifier', required = True, default = "0")
    arguments = argp.parse_args()

    dictForJson = {'device': str(arguments.number), 'seqNumber': 0, 'data': {}}

    while True:

        dictForJson['data']["temperature"] = generateTemp()
        dictForJson['data']["latitude"], dictForJson['data']["longitude"] = PT
        PT = get_nearby_point(PT)
        dictForJson["time"] = str(datetime.now())

        print("\nGenerated data ")
        print(str(dictForJson))
        sendData(dictForJson)

        time.sleep(randint(1,5))
