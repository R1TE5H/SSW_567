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


# Global Variables
github_user = "https://api.github.com/users/R1TE5H/repos"
commits_url = (
    "https://api.github.com/repos/R1TE5H/Data_Structures-Algorithms/commits"
)
list_of_repos = [
    {"name": "test_repo1"},
    {"name": "test_repo2"},
]
list_of_commits = [
    {"commit1": "commit1_comment"},
    {"commit2": "commit2_comment"},
]


# Tests (Valid API call simulations)
@patch("hw3.app.requests.get")
def test_fetch_github_data(mock_get):
    mocker = Mock()
    mocker.json.return_value = list_of_repos
    mock_get.return_value = mocker

    result = fetch_github_data(github_user)

    assert result is not None
    assert len(result) == 2
    assert result[0]["name"] == "test_repo1"
    assert result[1]["name"] == "test_repo2"


@patch("hw3.app.requests.get")
def test_fetch_repo_commits(mock_get):
    mocker = Mock()
    mocker.json.return_value = list_of_commits
    mock_get.return_value = mocker

    result = fetch_repo_commits(commits_url)

    assert result is not None
    assert len(result) == 2
    assert result[0]["commit1"] == "commit1_comment"
    assert result[1]["commit2"] == "commit2_comment"


@patch("hw3.app.requests.get")
def test_print_repo_commits_runs_without_error(mock_get):
    def fake_api_response(url, headers=None):
        mocker = Mock()
        if "repos" in url:
            mocker.json.return_value = list_of_repos
        else:
            mocker.json.return_value = list_of_commits
        return mocker

    mock_get.side_effect = fake_api_response
    print_repo_commits()


# Methods to test API call failures
#  First two are when there is an invalid URL
#  Second two are when there is a network error but valid URL
@patch("hw3.app.requests.get")
def test_fetch_github_data_negative_test(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_github_data("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_negative_test(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Network error"
    )

    result = fetch_repo_commits("invalid-url")
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_github_data_network_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_github_data(github_user)
    assert result is None


@patch("hw3.app.requests.get")
def test_fetch_repo_commits_network_error(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException(
        "Connection failed"
    )

    result = fetch_repo_commits(commits_url)
    assert result is None
