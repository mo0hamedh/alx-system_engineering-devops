#!/usr/bin/python3
"""
  function that queries the Reddit API and prints
  the titles of the first 10 .
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 .
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
        537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        for post in response.json().get('data').get('children')[:10]:
            print(post.get('data').get('title'))
