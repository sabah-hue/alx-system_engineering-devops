#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    # url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # response = requests.get(url, timeout=10, allow_redirects=False)
    # if response.status_code == 200:
    #     data = response.json()
    #     count = data['data']['subscribers']
    # else:
    #     count = 0
    # return count
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0
