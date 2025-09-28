import sys
import os
import requests
from unittest.mock import patch, Mock
from hw3.app import (
    fetch_github_data,
    fetch_repo_commits,
    print_repo_commits,
)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


github_user = "https://api.github.com/users/R1TE5H/repos"
commits_url = (
    "https://api.github.com/repos/R1TE5H/Data_Structures-Algorithms/commits"
)


@patch("hw3.app.requests.get")
def test_fetch_github_data_exists(mock_get):
    """Test that fetch_github_data returns data when API call succeeds"""
    mock_response = Mock()
    mock_response.json.return_value = [
        {"name": "test_repo1"},
        {"name": "test_repo2"},
    ]
    mock_get.return_value = mock_response

    result = fetch_github_data(github_user)

    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "test_repo1"
    assert result[1]["name"] == "test_repo2"


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_exists(mock_get):
    """Test that fetch_repo_commits returns data when API call succeeds"""
    mock_response = Mock()
    mock_response.json.return_value = [
        {"commit1": "commit1_comment"},
        {"commit2": "commit2_comment"},
    ]
    mock_get.return_value = mock_response

    result = fetch_repo_commits(commits_url)

    assert result is not None
    assert len(result) == 2
    assert result[0]["commit1"] == "commit1_comment"
    assert result[1]["commit2"] == "commit2_comment"


@patch("hw3.app.requests.get")
def test_fetch_github_data_with_invalid_url(mock_get):
    """Test fetch_github_data returns None when API call fails"""
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_github_data("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_with_invalid_url(mock_get):
    """Test fetch_repo_commits returns None when API call fails"""
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_repo_commits("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_print_repo_commits_runs_without_error(mock_get):
    """Test that print_repo_commits works with fake API responses"""

    def fake_api_response(url, headers=None):
        mock_response = Mock()
        if "repos" in url:
            mock_response.json.return_value = [
                {"name": "test_repo1"},
                {"name": "test_repo2"},
            ]
        else:
            mock_response.json.return_value = [
                {"commit1": "commit1_comment"},
                {"commit2": "commit2_comment"},
            ]
        return mock_response

    mock_get.side_effect = fake_api_response
    print_repo_commits()


@patch("hw3.app.requests.get")
def test_fetch_github_data_handles_errors(mock_get):
    """Test that fetch_github_data handles network errors gracefully"""
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_github_data(github_user)
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_handles_errors(mock_get):
    """Test that fetch_repo_commits handles network errors gracefully"""
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_repo_commits(commits_url)
    assert result is None
