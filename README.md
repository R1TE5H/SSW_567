# SSW 567

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/R1TE5H/SSW_567/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/R1TE5H/SSW_567/tree/main)

This is my repository for SSW 567 -- Quality Assurance and Maintenance

## Setup

To use the GitHub API functionality, you'll need to set up a GitHub Personal Access Token:

1. Copy `.env.example` to `.env`
2. Replace `your_github_token_here` with your actual GitHub token
3. The token will be loaded automatically when running the scripts

## Running Tests

To run tests, enter:
```bash
/Users/riteshpersaud/Desktop/SSW/567_code/.venv/bin/python -m pytest [PATH TO FILE OR DIR] -v -s
```

## Static Code Analysis & Coverage Reports

### Generating Pylint Report

To generate a comprehensive static code analysis report using Pylint:

```bash
# Generate pylint report for files in all directories (must list dirs)
PYTHONPATH=/Users/riteshpersaud/Desktop/SSW/567_code \
/Users/riteshpersaud/Desktop/SSW/567_code/.venv/bin/python -m pylint hw3 scripts tests \
--output-format=text --reports=yes > pylint_report.txt
```

### Generating Coverage Report

To generate a comprehensive code coverage report:

```bash
# Generate coverage report with HTML output (includes all directories)
/Users/riteshpersaud/Desktop/SSW/567_code/.venv/bin/python -m pytest tests/ --cov=hw3 --cov=scripts --cov=tests --cov=hw3/pylint_test --cov-report=term-missing --cov-report=html --cov-branch -v > coverage_report.txt

# View HTML coverage report (opens in browser)
open htmlcov/index.html
```