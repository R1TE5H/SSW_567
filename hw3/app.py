"""GitHub API interaction module for fetching repository data and commits."""

import os
from dotenv import load_dotenv

import requests

# Load environment variables from .env file
load_dotenv()

# Run File: source .venv/bin/activate && python hw3/github.py

auth = os.getenv("GITHUB_TOKEN", "")


def fetch_github_data(url, auth_token: str) -> list | None:
    """Fetch GitHub repository data from the given URL.

    Args:
        url: GitHub API URL to fetch data from
        auth_token: GitHub authentication token

    Returns:
        List of repository data or None if request fails
    """
    try:
        headers = {
            "Authorization": f"token {auth_token}",
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def fetch_repo_commits(url, auth_token: str) -> list | None:
    """Fetch commit data for a specific GitHub repository.

    Args:
        url: GitHub API URL for repository commits
        auth_token: GitHub authentication token

    Returns:
        List of commit data or None if request fails
    """
    try:
        headers = {
            "Authorization": f"token {auth_token}",
        }
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def print_repo_commits() -> None:
    """Print repository names and their commit counts for a GitHub user."""
    github_user = "https://api.github.com/users/R1TE5H/repos"
    commits_url = "https://api.github.com/repos/R1TE5H/{repo_name}/commits"

    data = fetch_github_data(github_user, auth)
    if data:
        for element in data:
            commits = (
                fetch_repo_commits(
                    commits_url.format(repo_name=element["name"]), auth
                )
                or []
            )

            print(f"Repo: {element['name']} Number of commits: {len(commits)}")

    else:
        print("Failed to fetch data.")


if __name__ == "__main__":
    print_repo_commits()
