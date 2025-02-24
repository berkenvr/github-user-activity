import os.path
import urllib.request
import os
import json


def load_github_activity_data(username):
    BASE_URL = f'https://api.github.com/users/{username}/events'
    response = urllib.request.urlopen(BASE_URL)

    if response.status == 200:
        response_data = response.read().decode('utf-8')
        event_data = json.loads(response_data)

        # Overrides existing file
        with open('data.json', 'w') as f:
            json.dump(event_data, f, indent = 4)


def print_github_activity(username):
    event_data = load_github_activity_data(username)
"""
CommitCommentEvent
CreateEvent
DeleteEvent
ForkEvent
GollumEvent
IssueCommentEvent
IssuesEvent
MemberEvent
PublicEvent
PullRequestEvent
PullRequestReviewEvent
PullRequestReviewCommentEvent
PullRequestReviewThreadEvent
PushEvent
ReleaseEvent
SponsorshipEvent
WatchEvent
"""

def main():
    print("hello world")
    try:
        while True:
            username = input('github-activity ')
            result = print_github_activity(username)
            print(result)
    except KeyboardInterrupt:
        print('\nUser-activity cli terminated')


if __name__ == '__main__':
    main()
