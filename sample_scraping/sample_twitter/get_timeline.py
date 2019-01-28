'''
get tweet sample
'''
import sys

import requests_oauthlib
import yaml


def load_yaml(filepath):
    with open(filepath) as f:
        data = yaml.load(f)
    return data


def main():
    filepath = '/Users/wararaki/.twitter/credential.yaml'
    credentials = load_yaml(filepath)

    # oauth
    twitter = requests_oauthlib.OAuth1Session(**credentials)

    # get timeline
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params ={'count' : 2, 'user_id': 'twitterjp'}
    response = twitter.get(url, params=params)

    # show timeline
    print(response.json())

    return 0


if __name__ == '__main__':
    sys.exit(main())
