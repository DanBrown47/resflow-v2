# github/utils.py
import re
import requests

def extract_github_username(github_url):
    match = re.search(r'github\.com/([^/]+)', github_url)
    if match:
        return match.group(1)
    return None

def fetch_github_profile(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data.get('name'),
            'public_repos': data.get('public_repos')
        }
    return None
