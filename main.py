import urllib.request
import json

event_dict =\
    {
        'CommitCommentEvent': 0,
        'CreateEvent': 0,
        'DeleteEvent': 0,
        'ForkEvent': 0,
        'GollumEvent': 0,
        'IssueCommentEvent': 0,
        'IssuesEvent': 0,
        'MemberEvent': 0,
        'PublicEvent': 0,
        'PullRequestEvent': 0,
        'PullRequestReviewEvent': 0,
        'PullRequestReviewCommentEvent': 0,
        'PullRequestReviewThreadEvent': 0,
        'PushEvent': 0,
        'ReleaseEvent': 0,
        'SponsorshipEvent': 0,
        'WatchEvent': 0
    }


def github_activity(username):
    BASE_URL = f'https://api.github.com/users/{username}/events'
    response = urllib.request.urlopen(BASE_URL)

    if response.status == 200:
        response_data = response.read().decode('utf-8')
        event_data = json.loads(response_data)

        # Overrides existing file
        with open('data.json', 'w') as f:
            json.dump(event_data, f, indent=4)

        return count_repos(event_data)


def count_events(event_data):
    temp_dict = {}

    for i in event_dict.keys():
        for j in range(len(event_data)):
            if event_data[j]['type'] == i:
                event_dict[i] += 1
                temp_dict.update({i: event_dict[i]})

    return temp_dict


def count_repos(event_data):
    temp_dict = {}

    for i in range(len(event_data)):
        event_type = event_data[i]['type']
        repo_name = event_data[i]['repo']['name']
        event = f'{event_type} to {repo_name}'

        if event not in temp_dict.keys():
            temp_dict.update({event: 1})
        else:
            temp_dict.update({event: temp_dict[event] + 1})

    return f'{temp_dict}'


def main():
    print("hello world")
    try:
        while True:
            username = input('github-activity ')
            result = github_activity(username)
            print(result)
    except KeyboardInterrupt:
        print('\nUser-activity cli terminated')


if __name__ == '__main__':
    main()
