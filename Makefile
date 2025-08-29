# Project metadata
PACKAGE_NAME=social-media-downloader
IMAGE_NAME=ghcr.io/nayandas69/$(PACKAGE_NAME)
VERSION=$(shell python -c "import tomllib; print(tomllib.load(open('pyproject.toml', 'rb'))['project']['version'])")

# Build Python package locally
install:
	pip install .

# Install in development mode
install-dev:
	pip install -e .[dev]

# Run the CLI locally
run:
	$(PACKAGE_NAME)

# Run tests
test:
	python -m pytest test/

# Format code
format:
	black smd/
	flake8 smd/

# Build Python package
build:
	python -m build

# Clean build artifacts
clean:
	rm -rf dist/ build/ *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Build Docker image
docker-build:
	docker build -t $(IMAGE_NAME):$(VERSION) -t $(IMAGE_NAME):latest .

# Run Docker image interactively
docker-run:
	docker run --rm -it -v $(PWD)/media:/app/media $(IMAGE_NAME):$(VERSION)

# Push Docker image to GHCR
docker-push:
	docker push $(IMAGE_NAME):$(VERSION)
	docker push $(IMAGE_NAME):latest

# Create and push Git tag
tag:
	git tag v$(VERSION)
	git push origin v$(VERSION)

# Help target
help:
	@echo "Available targets:"
	@echo "  install      - Install package locally"
	@echo "  install-dev  - Install in development mode"
	@echo "  run          - Run the CLI"
	@echo "  test         - Run tests"
	@echo "  format       - Format code with black and check with flake8"
	@echo "  build        - Build Python package"
	@echo "  clean        - Clean build artifacts"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container interactively"
	@echo "  docker-push  - Push Docker image to registry"
	@echo "  tag          - Create and push Git tag"

.PHONY: install install-dev run test format build clean docker-build docker-run docker-push tag help