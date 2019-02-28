#!/bin/bash

# Exit build script on first failure
set -e

# Echo commands to stdout.
set -x

# Run static analysis for Python bugs/cruft.
pyflakes setup.py bin/ ingredient_phrase_tagger/

# Run E2E tests.
bash ./test_e2e

echo "Build result: SUCCESS!"
