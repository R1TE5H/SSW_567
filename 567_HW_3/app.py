import requests

# Run File: source .venv/bin/activate && python app.py

auth_token = "Enter Security Token"


def fetch_github_data(url) -> list | None:
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


def fetch_repo_commits(url) -> list | None:
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


if __name__ == "__main__":
    github_user = "https://api.github.com/users/R1TE5H/repos"
    commits_url = "https://api.github.com/repos/R1TE5H/{repo_name}/commits"

    data = fetch_github_data(github_user)
    if data:
        for element in data:
            commits = fetch_repo_commits(
                commits_url.format(repo_name=element["name"])
            )
            if not commits:
                commits = []

            print(f"Repo: {element['name']} Number of commits: {len(commits)}")

    else:
        print("Failed to fetch data.")
