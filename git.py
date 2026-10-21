import requests


def fetch_repos(limit=10):
    url = "https://api.github.com/search/repositories"

    properties = {
        "q": "stars:>100",
        "sort": "updated",
        "order": "desc",
        "per_page": limit
    }

    try:
        response = requests.get(
            url,
            params=properties,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

    except requests.RequestException as error:
        print(f"Github request failed: {error}")
        return[]

    
    repositories = []

    for repo in data.get("items", []):

        repositories.append({
            "name": repo["full_name"],
            "description": repo.get("description") or "No description available",
            "url": repo["html_url"],
            "stars": repo["stargazers_count"],
            "language": repo.get("language") or "Unknown"
        })

    return repositories
