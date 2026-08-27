import requests
def fetch_gitignore(templates: list[str]) -> str:
    t = ",".join(templates)
    r = requests.get(f"https://www.toptal.com/developers/gitignore/api/{t}", timeout=15)
    r.raise_for_status()
    return r.text
