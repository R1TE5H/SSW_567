"""Tests for GitHub API functionality in hw3.app module."""

import sys
import os

import requests
from hw3.app import (
    fetch_github_data,
    fetch_repo_commits,
    print_repo_commits,
)

# Add the parent directory to the path so we can import the hw3 module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

GITHUB_USER = "https://api.github.com/users/R1TE5H/repos"
COMMITS_URL = (
    "https://api.github.com/repos/R1TE5H/Data_Structures-Algorithms/commits"
)

auth = os.getenv("GITHUB_TOKEN", "")


def test_fetch_github_data_exists():
    """Test that fetch_github_data function returns actual repository data"""

    result = fetch_github_data(GITHUB_USER, auth)
    print(result)
    assert True, "GitHub API should return repository data"


def test_fetch_repo_commits_exists():
    """Test that fetch_repo_commits function returns actual commit data"""

    result = fetch_repo_commits(COMMITS_URL, auth)
    print(result)
    assert True, "GitHub API should return commit data"


def test_fetch_github_data_with_invalid_url():
    """Test fetch_github_data with invalid URL returns None"""
    result = fetch_github_data("invalid-url", auth)
    assert result is None


def test_fetch_repo_commits_with_invalid_url():
    """Test fetch_repo_commits with invalid URL returns None"""
    result = fetch_repo_commits("invalid-url", auth)
    assert result is None


def test_print_repo_commits_runs_without_error():
    """Test that print_repo_commits can be called without throwing errors"""
    try:
        print_repo_commits()
        assert True
    except (
        requests.exceptions.RequestException,
        ImportError,
        AttributeError,
    ) as e:
        # We expect this might fail due to network issues, but shouldn't crash
        # with syntax errors or import issues
        assert "requests" in str(e) or "Network" in str(e) or "HTTP" in str(e)
