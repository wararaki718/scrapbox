'''
get tweet sample
'''
import json
import sys

import requests_oauthlib
import yaml


def load_yaml(filepath):
    with open(filepath) as f:
        data = yaml.load(f)
    return data

def get_user_info(twitter, user_id):
    url = 'https://api.twitter.com/1.1/users/show.json'
    params = {'user_id': user_id}
    return twitter.get(url, params=params)


def show_info(user):
    print(f'name       : {user.get("name")}')
    print(f'screen_name: {user.get("screen_name")}')
    print(f'followers  : {user.get("followers_count")}')
    print(f'following  : {user.get("friends_count")}')
    print('')


def main():
    filepath = '/Users/wararaki/.twitter/credential.yaml'
    credentials = load_yaml(filepath)

    # oauth
    twitter = requests_oauthlib.OAuth1Session(**credentials)

    # get timeline
    url = "https://api.twitter.com/1.1/followers/ids.json"
    params ={'count' : 5, 'user_id': 'twitterjp'}
    response = twitter.get(url, params=params)

    data = response.json()
    for follower_id in data['ids']:
        response = get_user_info(twitter, follower_id)
        show_info(response.json())
    print("DONE")

    return 0


if __name__ == '__main__':
    sys.exit(main())
