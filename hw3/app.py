import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Run File: source .venv/bin/activate && python hw3/github.py

auth = os.getenv("GITHUB_TOKEN", "")


def fetch_github_data(url, auth_token: str) -> list | None:
    try:
        headers = {
            "Authorization": f"token {auth_token}",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def fetch_repo_commits(url, auth_token: str) -> list | None:
    try:
        headers = {
            "Authorization": f"token {auth_token}",
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def print_repo_commits() -> None:
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
