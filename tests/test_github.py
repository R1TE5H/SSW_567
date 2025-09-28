import sys
import os
from hw3.app import (
    fetch_github_data,
    fetch_repo_commits,
    print_repo_commits,
)

# Add the parent directory to the path so we can import the hw3 module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

github_user = "https://api.github.com/users/R1TE5H/repos"
commits_url = (
    "https://api.github.com/repos/R1TE5H/Data_Structures-Algorithms/commits"
)

auth = os.getenv("GITHUB_TOKEN", "")


def test_fetch_github_data_exists():
    """Test that fetch_github_data function returns actual repository data"""
    # Debug: Check if token is available
    print(f"Token available: {bool(auth)}")
    print(f"Token length: {len(auth) if auth else 0}")

    result = fetch_github_data(github_user, auth)

    if not auth:
        # Skip test if no token is available
        import pytest

        pytest.skip("No GitHub token available - skipping API test")

    # Should return a list of repositories, not None
    assert result is not None, "GitHub API should return repository data"
    assert isinstance(result, list), "Result should be a list of repositories"
    assert len(result) > 0, "Should return at least one repository"


def test_fetch_repo_commits_exists():
    """Test that fetch_repo_commits function returns actual commit data"""
    # Debug: Check if token is available
    print(f"Token available: {bool(auth)}")
    print(f"Token length: {len(auth) if auth else 0}")

    result = fetch_repo_commits(commits_url, auth)

    if not auth:
        # Skip test if no token is available
        import pytest

        pytest.skip("No GitHub token available - skipping API test")

    # Should return a list of commits, not None
    assert result is not None, "GitHub API should return commit data"
    assert isinstance(result, list), "Result should be a list of commits"
    assert len(result) > 0, "Should return at least one commit"


def test_fetch_github_data_with_invalid_url():
    """Test fetch_github_data with invalid URL returns None"""
    result = fetch_github_data("invalid-url", auth)
    print(result)
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
    except Exception as e:
        # We expect this might fail due to network issues, but shouldn't crash
        # with syntax errors or import issues
        assert "requests" in str(e) or "Network" in str(e) or "HTTP" in str(e)
