# ==============================================================================
# Incident Learning Simulation - Makefile
# ==============================================================================
# Usage:
#   make lint       - Run linter (ruff)
#   make typecheck  - Run type checker (mypy)
#   make test       - Run tests
#   make check      - Run all checks (lint + typecheck + test)
#   make fix        - Auto-fix linting issues
# ==============================================================================

.PHONY: lint typecheck test check fix clean install

# Default Python
PYTHON ?= python3

# ==============================================================================
# Installation
# ==============================================================================
install:
	$(PYTHON) -m pip install -e ".[dev]"

install-dev:
	$(PYTHON) -m pip install ruff mypy pytest pytest-cov

# ==============================================================================
# Linting (Ruff)
# ==============================================================================
lint:
	@echo "Running ruff linter..."
	$(PYTHON) -m ruff check model.py tests/

lint-fix:
	@echo "Auto-fixing lint issues..."
	$(PYTHON) -m ruff check --fix model.py tests/

fix: lint-fix

# ==============================================================================
# Type Checking (Mypy)
# ==============================================================================
typecheck:
	@echo "Running mypy type checker..."
	$(PYTHON) -m mypy model.py

type: typecheck

# ==============================================================================
# Testing
# ==============================================================================
test:
	@echo "Running tests..."
	$(PYTHON) -m pytest tests/ -v

test-cov:
	@echo "Running tests with coverage..."
	$(PYTHON) -m pytest tests/ -v --cov=. --cov-report=term-missing

test-quick:
	@echo "Running quick test..."
	$(PYTHON) -m unittest tests.test_model -v

# ==============================================================================
# Combined Checks
# ==============================================================================
check: lint typecheck test
	@echo "All checks passed!"

ci: check
	@echo "CI checks complete."

# ==============================================================================
# Cleanup
# ==============================================================================
clean:
	rm -rf __pycache__ tests/__pycache__ .pytest_cache .mypy_cache .ruff_cache
	rm -rf *.egg-info .coverage htmlcov
	find . -name "*.pyc" -delete

# ==============================================================================
# Run Simulation
# ==============================================================================
run:
	$(PYTHON) model.py

run-experiments:
	$(PYTHON) run_experiments.py
