## Herramientas de Construcción

#### MAKEFILE

La herramienta Make permite, a través del archivo Makefile, configurar una herramienta de construcción para python. Pese a que esta herramienta está pensada para construir código C/C++, se puede utilizar también para python, y su configuración es bastante intuitiva y sencilla por lo que es una buena opción.

Las diferentes órdenes que podemos ejecutar:

 - make clean	# limpiar directorio actual
 - make test	# pasar tests
 - make install	# instalar dependencias, sólo si es la primera vez
 - make run	# levantar microservicio
 - make device	# lanzar un dispositivo

Descrición del archivo:

	# En primer lugar, indicamos a Make que las siguientes órdenes
	# corresponden a comandos de ejecución y no archivos a construir,
	# que son los targets por defecto en un Makefile

	.PHONY: clean test install run device

	# Para lanzar varios devices, podemos cambiar este número y
	# volver a ejecutar make device
	
	NUM_DEVICE=5

	# Limpiar directorio, borrando archivos copia de seguridad y la
	# caché creada por defecto en python
	
	clean:
		rm -f "*~"
		rm -rf "__pycache__"

	# Lanzar tests, llamando previamente a clean
	
	test: clean
		python3 -m pytest tests/test_data.py

	# Instalar dependencias
	
	install:
		pip3 install --user -r requirements.txt

	# Levantar el microservicio
	
	run: test
		python3 src/AsyncService.py

	# Lanzar un dispositivo, con el id indicado al inicio
	
	device:
		python3 src/device.py -n $(NUM_DEVICE)



#### PIP & requirements.txt

- El gestor de paquetes de python, PIP, instalará los paquetes que se encuentren indicados en el archivo requirements.txt

 - En el archivo previamente mencionado, se incluirá el nombre de todos los paquetes necesarios para el correcto funcionamiento de la aplicación. Más adelante, se concretarán las versiones, indicando para cada paquete la versión que se ha de instalar.
