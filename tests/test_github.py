import sys
import os
from unittest.mock import patch, Mock
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


@patch("hw3.app.requests.get")
def test_fetch_github_data_exists(mock_get):
    """Test that fetch_github_data returns data when API call succeeds"""
    # Create a fake successful response
    mock_response = Mock()
    mock_response.json.return_value = [{"name": "test_repo"}]
    mock_get.return_value = mock_response

    result = fetch_github_data(github_user)

    assert result is not None
    assert len(result) == 1
    assert result[0]["name"] == "test_repo"


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_exists(mock_get):
    """Test that fetch_repo_commits returns data when API call succeeds"""
    # Create a fake successful response
    mock_response = Mock()
    mock_response.json.return_value = [{"sha": "abc123"}]
    mock_get.return_value = mock_response

    result = fetch_repo_commits(commits_url)

    assert result is not None
    assert len(result) == 1
    assert result[0]["sha"] == "abc123"


@patch("hw3.app.requests.get")
def test_fetch_github_data_with_invalid_url(mock_get):
    """Test fetch_github_data returns None when API call fails"""
    import requests

    # Make requests.get throw a network error
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_github_data("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_with_invalid_url(mock_get):
    """Test fetch_repo_commits returns None when API call fails"""
    import requests

    # Make requests.get throw a network error
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_repo_commits("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_print_repo_commits_runs_without_error(mock_get):
    """Test that print_repo_commits works with fake API responses"""

    # Create different fake responses based on what URL is called
    def fake_api_response(url, headers=None):
        mock_response = Mock()
        if "repos" in url:
            # Fake repo list
            mock_response.json.return_value = [{"name": "my_repo"}]
        else:
            # Fake commits for any repo
            mock_response.json.return_value = [{"sha": "abc123"}]
        return mock_response

    mock_get.side_effect = fake_api_response

    # This should work without errors
    print_repo_commits()


@patch("hw3.app.requests.get")
def test_fetch_github_data_handles_errors(mock_get):
    """Test that fetch_github_data handles network errors gracefully"""
    import requests

    # Simulate a network error
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_github_data(github_user)
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_handles_errors(mock_get):
    """Test that fetch_repo_commits handles network errors gracefully"""
    import requests

    # Simulate a network error
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_repo_commits(commits_url)
    assert result is None
