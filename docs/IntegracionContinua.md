## Integración Continua

##### Tests

Se incorporan tests para comprobar el correcto funcionamiento de la clase Data. Estos objetos serán empleados en el servidor para trabajar con los datos recibidos.

También se testea el correcto funcionamiento del servicio. Para ello, se ha de levantar el servidor y posteriormente lanzar los tests, que emplean una especie de mock. Se mandará al servidor un device predeterminado, y se comprobará a través de un get que el valor devuelto por la URL correspondiente corresponde con el enviado a través del canal de comunicación de socketIO.


##### Travis

Se linkea Travis-CI con el repositorio para la ejecución de tests de integración continua. 

Se añade, además, el archivo .travis.yml, que se configura de manera que el entorno de ejecución de los tests sea igual al empleado en local durante las pruebas. 

En el mismo archivo se lleva a cabo la construcción empleando la instalación de dependencias con pip3 y el archivo donde indicamos los paquetes de python necesarios para ejecutar correctamente la aplicación.

Pasamos a explicar la configuración del fichero .travis.yml:

	language: python	# indicamos el lenguaje de programación de la aplicación a testear

	python:
	  - "3.6"		# Establecemos la versión de python utilizada, para
	  			# evitar posibles problemas con otras versiones

	install:
	  - pip3 install -r requirements.txt		# Instalamos dependencias,
	  					# indicadas en el archivo requirements.txt

	before_script:
  	  - python3 src/AsyncService.py & 	#Lanzamos el servicio para
  	  - sleep 5s					# testearlo con nuestro device mockeado
  	            					# Esperar 5 segundos para que levante el servicio

	script:
	  - python3 -m pytest tests/test_data.py	# Comando para lanzar tests


##### Circle

Vamos a configurar la versión grautita de Circle CI, que tan solo permitirá ejecutar 1 trabajo en cada instante y trabajar con un único contenedor. 

Pasamos a explicar la configuración del fichero .circleci/config.yml:

	version: 2	# Versión (2, 2.0 o 2.1) En este caso, la versión no
	# simplifica el archivo ni reutiliza configuraciones por defecto.
	# Además nos notificará de los cambios conflictivos.
	
	jobs: 	# Comienza la definición del 'trabajo' a ejecutar
	
	build:	# Es necesario indicar en caso de no usar workflws o flujos

	working_directory: ~/IoT_AsyncService	# Directorio de trabajo

	docker:	# Pasamos a configurar nuestro contenedor, donde se
			# ejecutarán nuestros tests
	
	- image: circleci/python:3.6.8	# circleci nos ofrece varias
	# imagenes base para nuestro contenedor según el lenguaje que
	# vayamos a utilizar. En nuestro caso, utilizaremos la de python
	# indicando la etiqueta con la versión correspondiente a la
	# instalada localmente, dónde se ha probado la app y funciona
	# correctamente. Las imágenes se pueden consultar en la web
	# oficial de circleCI.
	
	steps:	# Conjunto de pasos a realizar, codificados mediante
			# pares clave : valor
	
	- checkout	# Pasar el código al directorio de trabajo
	
	- restore_cache:    #Rescatamos paquetes cacheados
          	key: deps1-{{ .Branch }}-{{ checksum "requirements.txt" }}
	
	- run:
        command: |		# Comando a ejecutar vía shell
          pip3 install -r requirements.txt

	- run:
        command: |     #Comando a ejecutar vía shell
          python3 src/AsyncService.py &
	- run:
        command: |     #Comando a ejecutar vía shell
          sleep 5s     #Esperar 5 segundos para que el server se levante
          			
	- save_cache:	
        key: deps1-{{ .Branch }}{{ checksum "requirements.txt" }}
        paths:
          - ".circleci/cache"
        	
			# Cacheamos los paquetes para no reinstalarlos.
			# Indicamos la ruta, la rama actual y el archivo, el cual puede
			# indicarse como un hash SHA256 codificado en base64.
			
	- run:
        command: |		# Lanzar tests
          python3 -m pytest tests/test_data.py
          
	- store_test_results:     #Guardar resultado tras la ejecución
          path: "test-results"
