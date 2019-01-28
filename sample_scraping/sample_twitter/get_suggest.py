'''
get suggest sample
'''
import json
import sys

import requests_oauthlib
import yaml


def load_yaml(filepath):
    with open(filepath) as f:
        data = yaml.load(f)
    return data


def show_user(user):
    print(f'name       : {user.get("name")}')
    print(f'screen_name: {user.get("screen_name")}')
    print(f'followers  : {user.get("followers_count")}')
    print(f'following  : {user.get("friends_count")}')
    print('')


def show_users(users):
    for user in users[:2]:
        show_user(user)


def show_tweet(status):
    print(f'create_date: {status.get("created_at")}')
    print(f'tweet      : {status.get("text")}')
    print("")


def show_info(user_objs):
    for user_obj in user_objs:
        show_user(user_obj)
        show_tweet(user_obj.get('status'))


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
        print(f'suggest: {suggestion}')
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
        show_info(data)
    print("DONE")

    return 0


if __name__ == '__main__':
    sys.exit(main())
