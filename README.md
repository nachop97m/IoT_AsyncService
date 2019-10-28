IoT_AsyncService
===================

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/nachop97m/IoT_AsyncService.svg?branch=master)](https://travis-ci.com/nachop97m/IoT_AsyncService) [![CircleCI](https://circleci.com/gh/nachop97m/IoT_AsyncService.svg?style=svg)](https://circleci.com/gh/nachop97m/IoT_AsyncService)


## Descripción del Servicio

Proyecto para Infraestructura Virtual 19-20 UGR, consistente en un microservicio para la recepción de metadatos de un IoT device en tiempo real. 

Para este propósito, se desarrollará un script en python que emulará un dispositivo IoT. Este dispositivo generará datos aleatorios que serán enviados de manera asíncrona, y serán recibidos por un microservicio (back-end).

Una vez el back reciba los datos a través de dicho servicio, éstos podrían procesarse, almacenarse en una Base de Datos o enviarse a un Front-End para su visualización; en nuestro caso, simplemente se mostrarán en formato JSON a través de una URL, por lo que se usará también un framework web (flask). 

Por último, se empleará socketIO para la recepción asícrona de mensajes desde el IoT device. Licencia GNU estandar v3.0 (Software Libre).


## Herramientas

- El desarrollo de la aplicación se realizará en python, y se utilizará flask como framework web y socketIO para la recepción asíncrona de mensajes.

- Para el desarrollo de la aplicación, la idea era utilizar Pycharm, que además incluye soporte para git pero, al haber cumplido el período de prueba y dado su elevado coste,  se desarrollará utilizando el editor ATOM.

- Implementación de test para la herramienta pytest.

- Uso de Travis y Circle para los tests de integración continua.

- Se valora la posibilidad de incorporar una pequeña Base de Datos MongoDB para que el microservicio almacene los datos que obtiene del dispositivo IoT.

- geoJSON.io para obtener manualmente localizaciones de dispositivos en formato JSON.


### Requirements


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

- requests

### Integración Continua

Nos decantamos por TravisCI y CircleCI. Para éste último, nos damos de alta en su web con la versión gratuita. En ambos casos la puesta en marcha radica en enlazar ambas herramientas con el repositorio, en el que previamente se ha añadido un archivo de configuración específico para nuestra aplicación. Para más información, consultar la documentación específica: 

- [Integración Continua](https://github.com/nachop97m/IoT_AsyncService/blob/master/docs/IntegracionContinua.md)


### Herramientas de construcción

	buildtool: Makefile

Para la construcción del proyecto, nos decantamos por Make. Incluimos un archivo Makefile con las directivas necesarias para instalar, levantar y parar nuestro microservicio. A continuación, se encuentra la información más detallada:

- [Herramientas de Construcción](https://github.com/nachop97m/IoT_AsyncService/blob/master/docs/HerramientasConstruccion.md)


### Ejecución

Rutas definidas:

	/
	/status
	/last_received

Las rutas incluidas de momento en este microservicio son dos: una que indica el status de la aplicación y otra que devuelve el último dato obtenido de un dispositivo ("/" redirige a /last_received). Este microservicio puede ser implementado en cualquier aplicación con un front-end que reciba los datos y, por ejemplo, los muestre en un mapa o una gráfica.


### PaaS

El PaaS elegido para desplegar la aplicación será heroku. Una vez registrados, la herramienta permite levantar el servicio en local gracias a su CLI, o directamente en remoto. Además, Heroku es gratuito por lo que es un punto a favor para nuestro propósito de aprendizaje en esta asignatura.

- [Documentación despliegue en Heroku](https://github.com/nachop97m/IoT_AsyncService/blob/master/docs/Heroku.md)