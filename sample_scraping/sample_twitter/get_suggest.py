'''
get suggest sample
'''
import sys

import requests_oauthlib
import yaml


def load_yaml(filepath):
    with open(filepath) as f:
        data = yaml.load(f)
    return data


def show_users(users):
    for user in users[:2]:
        print(f'name       : {user.get("name")}')
        print(f'screen_name: {user.get("screen_name")}')
        print(f'followers  : {user.get("followers_count")}')
        print(f'following  : {user.get("friends_count")}')
        print('')


def show_tweet(tweet):
    print(tweet)


def main():
    filepath = '/Users/wararaki/.twitter/credential.yaml'
    credentials = load_yaml(filepath)

    # oauth
    twitter = requests_oauthlib.OAuth1Session(**credentials)

    # get suggest_category
    url = "https://api.twitter.com/1.1/users/suggestions.json"
    response = twitter.get(url)
    suggestions = response.json()

    # show suggest users
    print('show suggest users')
    for suggestion in suggestions[:5]:
        slug = suggestion.get('slug')

        # show suggest users
        url = f'https://api.twitter.com/1.1/users/suggestions/{slug}.json'
        response = twitter.get(url)
        data = response.json()
        show_users(data.get('users'))

    # show suggset tweet
    print('show suggest tweet')
    for suggestion in suggestions[:5]:
        slug = suggestion.get('slug')

        # show suggest tweet
        url = f'https://api.twitter.com/1.1/users/suggestions/{slug}/members.json'
        response = twitter.get(url)
        data = response.json()
        show_tweet(data.get('status'))

    return 0


if __name__ == '__main__':
    sys.exit(main())
