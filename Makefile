COMPOSE := docker compose
LOCAL_URL := http://localhost:8080/physics-lab/

.PHONY: help engine-start engine-stop setup serve start stop restart logs status shell build

help:
	@echo "make setup    Build the local Docker image"
	@echo "make engine-start  Start Colima (macOS Homebrew setup)"
	@echo "make engine-stop   Stop Colima"
	@echo "make serve    Run the development server in the foreground"
	@echo "make start    Run the development server in the background"
	@echo "make stop     Stop the development server"
	@echo "make restart  Restart the development server"
	@echo "make logs     Follow development server logs"
	@echo "make status   Show container status"
	@echo "make shell    Open a shell in the running container"
	@echo "make build    Generate the production site in _site/"
	@echo "Local URL: $(LOCAL_URL)"

engine-start:
	colima start --cpu 2 --memory 4 --disk 30

engine-stop:
	colima stop

setup:
	$(COMPOSE) build

serve:
	$(COMPOSE) up

start:
	$(COMPOSE) up --detach
	@echo "Open $(LOCAL_URL)"

stop:
	$(COMPOSE) down

restart:
	$(COMPOSE) down
	$(COMPOSE) up --detach
	@echo "Open $(LOCAL_URL)"

logs:
	$(COMPOSE) logs --follow

status:
	$(COMPOSE) ps

shell:
	$(COMPOSE) exec jekyll bash

build:
	$(COMPOSE) run --rm jekyll bundle exec jekyll build
