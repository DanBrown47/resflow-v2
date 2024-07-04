import os
import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Resume
from github.utils import extract_github_username, fetch_github_profile

@receiver(post_save, sender=Resume)
def fetch_github_details(sender, instance, created, **kwargs):
    if created and instance.github_url:
        username = extract_github_username(instance.github_url)
        if username:
            profile_data = fetch_github_profile(username)
            if profile_data:
                profile_path = os.path.join('media', 'profile', f'{username}.json')
                os.makedirs(os.path.dirname(profile_path), exist_ok=True)
                with open(profile_path, 'w') as profile_file:
                    json.dump(profile_data, profile_file)
