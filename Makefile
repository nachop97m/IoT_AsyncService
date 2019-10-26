.PHONY: clean test install run device

NUM_DEVICE=5

clean:
	rm -f "*~"
	rm -rf "__pycache__"

test:
	python3 -m pytest tests/test_data.py

install:
	pip3 install --user -r requirements.txt

run:
	python3 src/AsyncService.py

device:
	python3 src/device.py -n $(NUM_DEVICE)
