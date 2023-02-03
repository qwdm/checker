
run_prom:
	sh run_prom.sh

build:
	docker build -t checker .

run:
	docker run --network="host" checker
