IoT_AsyncService
===================

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Descripción del Servicio

Proyecto para Infraestructura Virtual 19-20 UGR, consistente en un microservicio para la recepción de metadatos de un IoT device en tiempo real. 

Para este propósito, se desarrollará un script en python que emulará un dispositivo IoT. Este dispositivo generará datos aleatorios que serán enviados de manera asíncrona, y serán recibidos por un microservicio (back-end).

Una vez el back reciba los datos a través de dicho servicio, éstos podrían procesarse, almacenarse en una Base de Datos o enviarse a un Front-End para su visualización; en nuestro caso, simplemente se mostrarán en formato JSON a través de una URL, por lo que se usará también un framework web (flask). 

Por último, se empleará socketIO para la recepción asícrona de mensajes desde el IoT device. Licencia GNU estandar v3.0 (Software Libre).


## Herramientas

- El desarrollo de la aplicación se realizará en python, y se utilizará flask como framework web y socketIO para la recepción asíncrona de mensajes.

- Makefile.

- Para el desarrollo de la aplicación, la idea era utilizar Pycharm, que además incluye soporte para git pero, al haber cumplido el período de prueba y dado su elevado coste,  se desarrollará utilizando el editor ATOM.


## Requirements

- Python3

- Flask

- SocketIO (pip install "python-socketio[client]")

- Geopy (pip install geopy)