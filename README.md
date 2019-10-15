IoT_AsyncService
===================

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.org/nachop97m/IoT_AsyncService.svg?branch=master)](https://travis-ci.com/nachop97m/IoT_AsyncService)


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

Se linkea Travis-CI con el repositorio para la ejecución de tests de integración continua. 

Se añade, además, el archivo .travis.yml, que se configura de manera que el entorno de ejecución de los tests sea igual al empleado en local durante las pruebas. 

En el mismo archivo se lleva a cabo la construcción empleando la instalación de dependencias con pip3 y el archivo donde indicamos los paquetes de python necesarios para ejecutar correctamente la aplicación.

##### Circle

Vamos a configurar la versión grautita de Circle CI, que tan solo permitirá ejecutar 1 trabajo en cada instante y trabajar con un único contenedor. 

Pasamos a explicar la configuración del fichero .circleci/config.yml:

	version: 2	# Versión (2, 2.0 o 2.1) En este caso, la versión no simplifica el archivo ni reutiliza configuraciones por defecto. Además nos notificará de los cambios conflictivos.
	
	jobs: 	# Comienza la definición del 'trabajo' a ejecutar
	
	build:	# Es necesario indicar en caso de no usar workflws o flujos

	docker:	# Pasamos a configurar nuestro contenedor, donde se ejecutarán nuestros tests
	
	- image: circleci/python:3.6.8	# circleci nos ofrece varias imagenes base para nuestro contenedor según el lenguaje que vayamos a utilizar. En nuestro caso, utilizaremos la de python indicando la etiqueta con la versión correspondiente a la instalada localmente, dónde se ha probado la app y funciona correctamente. Las imágenes se pueden consultar en la web oficial de circleCI.
	
	steps:	# Conjunto de pasos a realizar, codificados mediante pares clave : valor
	
	- checkout	# Pasar el código al directorio de trabajo
	
	- run:
        command: |		# Comando a ejecutar vía shell
          pip3 install -r requirements.txt
          
	  - save_cache:	
        	key: deps1-{{ .Branch }}{{ checksum "requirements.txt" }}
        	
			# Cacheamos los paquetes para no reinstalarlos. Indicamos la rama actual y el archivo, el cual puede indicarse como un hash SHA256 codificado en base64.
			
	- run:
        command: |		# Lanzar tests
          python3 -m pytest tests/test_data.py
          
	- store_test_results:     #Guardar resultado tras la ejecución
          path: test-results