import requests


def get_data(url):
    results = []

    while url:
        response = requests.get(url, timeout=15)

        if response.status_code == 409:
            if response.json().get("message") == "Git Repository is empty.":
                return []

        response.raise_for_status()
        results.extend(response.json())
        url = response.links.get("next", {}).get("url")

    return results


def get_repositories(username):
    if not isinstance(username, str) or not username.strip():
        raise ValueError("Enter a GitHub username.")

    username = username.strip()
    repos = get_data(
        f"https://api.github.com/users/{username}/repos?per_page=100"
    )

    results = []

    for repo in repos:
        name = repo["name"]
        commits = get_data(
            f"https://api.github.com/repos/{username}/{name}/commits?per_page=100"
        )
        results.append((name, len(commits)))

    return results


if __name__ == "__main__":
    username = input("Enter GitHub username: ")

    try:
        results = get_repositories(username)

        if not results:
            print("No repositories found.")

        for name, count in results:
            print(f"Repo: {name} Number of commits: {count}")

    except (requests.RequestException, ValueError) as error:
        print(f"Error: {error}")