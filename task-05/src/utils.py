import json
import os
import requests
import random
from rich.console import Console

console = Console()
PROFILE_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "profiles.json")

def load_profiles():
    try:
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users": []}

def save_profiles(profiles):
    try:
        with open(PROFILE_FILE, "w") as f:
            json.dump(profiles, f, indent=4)
    except OSError:
        pass

def get_profile(username):
    return next((user for user in load_profiles()["users"] if user["username"] == username), None)

def update_profile(new_profile):
    profiles = load_profiles()
    users = profiles["users"]
    for i, user in enumerate(users):
        if user["username"] == new_profile["username"]:
            users[i] = new_profile
            break
    else:
        users.append(new_profile)
    save_profiles(profiles)

def get_categories():
    try:
        response = requests.get("https://opentdb.com/api_category.php", timeout=5)
        response.raise_for_status()
        return response.json().get("trivia_categories", [])
    except requests.RequestException as e:
        console.print(f"[red]Error fetching categories: {e}[/red]")
        return [{"id": random.randint(9, 32), "name": "Random Category"}]