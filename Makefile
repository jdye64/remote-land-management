# IMAGE_NAME=fastapi-weather-app
# CONTAINER_NAME=fastapi-weather-container
# PORT=5000

.PHONY: build run

build:
	docker compose build

run:
	docker compose up
