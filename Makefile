#Makefile for IoT Async Service. 1st stage.

.PHONY: clean test install run device

NUM_DEVICE=5

clean:
	rm -f "*~"
	rm -rf "__pycache__"

test: clean
	python3 -m pytest tests/test_data.py

install:
	pip3 install --user -r requirements.txt

run: test
	python3 src/AsyncService.py

device:
	python3 src/device.py -n $(NUM_DEVICE)
