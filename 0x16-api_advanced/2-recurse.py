#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """prints the titles of all hot articles"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, timeout=10,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        count = data['data']['children']
        for i in count:
            hot_list.append(i['data']['title'])
        if data['data']['after']:
            recurse(subreddit, hot_list)
        return hot_list
    else:
        print('None')
