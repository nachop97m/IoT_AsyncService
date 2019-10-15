IoT_AsyncService
===================

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Build Status](https://travis-ci.org/nachop97m/IoT_AsyncService.svg?branch=master)](https://travis-ci.com/nachop97m/IoT_AsyncService)


## Descripción del Servicio

Proyecto para Infraestructura Virtual 19-20 UGR, consistente en un microservicio para la recepción de metadatos de un IoT device en tiempo real. 

Para este propósito, se desarrollará un script en python que emulará un dispositivo IoT. Este dispositivo generará datos aleatorios que serán enviados de manera asíncrona, y serán recibidos por un microservicio (back-end).

Una vez el back reciba los datos a través de dicho servicio, éstos podrían procesarse, almacenarse en una Base de Datos o enviarse a un Front-End para su visualización; en nuestro caso, simplemente se mostrarán en formato JSON a través de una URL, por lo que se usará también un framework web (flask). 

Por último, se empleará socketIO para la recepción asícrona de mensajes desde el IoT device. Licencia GNU estandar v3.0 (Software Libre).


## Herramientas

- El desarrollo de la aplicación se realizará en python, y se utilizará flask como framework web y socketIO para la recepción asíncrona de mensajes.

- Para el desarrollo de la aplicación, la idea era utilizar Pycharm, que además incluye soporte para git pero, al haber cumplido el período de prueba y dado su elevado coste,  se desarrollará utilizando el editor ATOM.

- Implementación de test para la herramienta pytest.

- Uso de Travis para los tests de integración continua.

- Se valora la posibilidad de incorporar una pequeña Base de Datos MongoDB para que el microservicio almacene los datos que obtiene del dispositivo IoT.

- geoJSON.io para obtener manualmente localizaciones de dispositivos en formato JSON.


## Requirements


##### IoT Device Emulator:

- Python3

- Flask

- SocketIO

- Geopy


##### IoT Async Service & Data manager:

- Python3

- Flask-SocketIO


##### Tests

- pytest


## Integración Continua

##### Travis

Se linkea Travis-CI con el repositorio para la ejecución de tests de integración continua. Se añade, además, el archivo .travis.yml, que se configura de manera que el entorno de ejecución de los tests sea igual al empleado en local durante las pruebas. En el mismo archivo se lleva a cabo la construcción empleando la instalación de dependencias con pip3 y el archivo donde indicamos los paquetes de python necesarios para ejecutar correctamente la aplicación