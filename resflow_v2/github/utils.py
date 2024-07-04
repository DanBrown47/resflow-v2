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
        user_data = response.json()
        repos_url = user_data['repos_url']
        repos_response = requests.get(repos_url)
        repos_data = repos_response.json() if repos_response.status_code == 200 else []

        return {
            'username': username,
            'full_name': user_data.get('name'),
            'avatar_url': user_data.get('avatar_url'),
            'bio': user_data.get('bio'),
            'location': user_data.get('location'),
            'email': user_data.get('email'),
            'company': user_data.get('company'),
            'blog': user_data.get('blog'),
            'twitter_username': user_data.get('twitter_username'),
            'public_repos': user_data.get('public_repos'),
            'public_gists': user_data.get('public_gists'),
            'followers': user_data.get('followers'),
            'following': user_data.get('following'),
            'created_at': user_data.get('created_at'),
            'updated_at': user_data.get('updated_at'),
            'repositories': [
                {
                    'name': repo.get('name'),
                    'description': repo.get('description'),
                    'fork': repo.get('fork'),
                    'url': repo.get('html_url'),
                    'stars': repo.get('stargazers_count'),
                    'forks': repo.get('forks_count'),
                    'watchers': repo.get('watchers_count'),
                    'language': repo.get('language'),
                    'created_at': repo.get('created_at'),
                    'updated_at': repo.get('updated_at'),
                    'size': repo.get('size'),
                    'default_branch': repo.get('default_branch'),
                    'open_issues_count': repo.get('open_issues_count'),
                    'has_issues': repo.get('has_issues'),
                    'has_wiki': repo.get('has_wiki'),
                    'has_pages': repo.get('has_pages'),
                    'license': {
                        'name': repo['license']['name'] if repo['license'] else None,
                        'spdx_id': repo['license']['spdx_id'] if repo['license'] else None,
                        'url': repo['license']['url'] if repo['license'] else None
                    } if repo.get('license') else None
                } for repo in repos_data
            ]
        }
    return None
