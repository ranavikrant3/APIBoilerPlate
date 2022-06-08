APP_NAME      = pmk-inference-gateway

# --------------------------------------------------------------------
# Task : Docker management
# --------------------------------------------------------------------


# Build the container
build:
	@docker build -t $(APP_NAME) .

# Run the container
run:
	@docker run --detach -p 8000:5000 --name=$(APP_NAME) $(APP_NAME)

## Stop and remove a running container
kill:
	@echo 'Killing container...'
	@docker stop $(APP_NAME)
	@docker rm $(APP_NAME)

# Remove the image from Docker
clean:
	@docker image rm $(APP_NAME)

# Accessing the cli from Docker
cli:
	@docker exec -it $(APP_NAME) /bin/bash
