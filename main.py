import urllib.request
import urllib.error
import json

def fetch_github_activity(username):
    BASE_URL = f'https://api.github.com/users/{username}/events'

    try:
        with urllib.request.urlopen(BASE_URL) as response:
            if response.status != 200:
                print(f'Error: {response.status}')
                return None
            response_data = response.read().decode('utf-8')
            return json.loads(response_data)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print('User not found')
        else:
            print(f'HTTP Error: {e.code}')
    except urllib.error.URLError as e:
        print(f"Failed to reach the server: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def display_activity(event_data):
    if not event_data:
        print('No activity found')
        return

    for event in event_data:
        event_type = event.get('type', 'UnknownType')
        event_repo = event.get('repo', {}).get('name', 'UnknownRepo')
        
        if event_type == "PushEvent":
            commits = event.get("payload", {}).get("commits", [])
            count = len(commits)
            print(f"Pushed {count} commit{'s' if count != 1 else ''} to {event_repo}")
        elif event_type == "IssuesEvent":
            action = event.get("payload", {}).get("action", "did something with")
            print(f"{action.capitalize()} an issue in {event_repo}")
        elif event_type == "WatchEvent":
            print(f"Starred {event_repo}")
        elif event_type == "ForkEvent":
            print(f"Forked {event_repo}")
        elif event_type == "PullRequestEvent":
            action = event.get("payload", {}).get("action", "did something with")
            print(f"{action.capitalize()} a pull request in {event_repo}")
        else:
            print(f"{event_type} in {event_repo}")

def main():
    print("hello world")
    try:
        while True:
            username = input('github-activity ')
            display_activity(fetch_github_activity(username))
    except KeyboardInterrupt:
        print('\nUser-activity cli terminated')

if __name__ == '__main__':
    main()
