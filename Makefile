# Project metadata
PACKAGE_NAME=social-media-downloader
IMAGE_NAME=ghcr.io/nayandas69/$(PACKAGE_NAME)
VERSION=$(shell python -c "import toml; print(toml.load('pyproject.toml')['project']['version'])")

# Build Python package locally
install:
	pip install .

# Run the CLI locally
run:
	$(PACKAGE_NAME)

# Build Docker image
docker-build:
	docker build -t $(IMAGE_NAME):$(VERSION) .

# Run Docker image
docker-run:
	docker run --rm $(IMAGE_NAME):$(VERSION)

# Publish Docker image to GHCR
docker-push:
	docker push $(IMAGE_NAME):$(VERSION)

# Tag Git version
tag:
	git tag $(VERSION)
	git push origin $(VERSION)

# Clean cache (optional)
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf dist *.egg-info