## Herramientas de Construcción

##### MAKEFILE

La herramienta Make permite, a través del archivo Makefile, configurar una herramienta de construcción para python. Pese a que esta herramienta está pensada para construir código C/C++, se puede utilizar también para python, y su configuración es bastante intuitiva y sencilla por lo que es una buena opción.

	.PHONY: clean test install run device

	NUM_DEVICE=5

	clean:
		rm -f "*~"

	test:
		python3 -m pytest tests/test_data.py

	install:
		pip3 install --user -r requirements.txt

	run:
		python3 src/AsyncService.py

	device:
		python3 src/device.py -n $(NUM_DEVICE)

##### PIP & requirements.txt

- El gestor de paquetes de python, PIP, instalará los paquetes que se encuentren indicados en el archivo requirements.txt

 - En el archivo previamente mencionado, se incluirá el nombre de todos los paquetes necesarios para el correcto funcionamiento de la aplicación. Más adelante, se concretarán las versiones, indicando para cada paquete la versión que se ha de instalar.
