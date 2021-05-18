#!/usr/bin/python3
"""Function to GET the top 10 hot posts in a agiven subreddit"""
from requests import get, exceptions


def top_ten(subreddit):
    """Use GET request to find the top 10 hot posts in `subreddit`"""
    try:
        r = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                headers={"User-Agent": "python:holberton project by 2244"},
                params={"limit": 10},
                allow_redirects=False)
        r.raise_for_status()
    except exceptions.RequestException as e:
        print("None")
    else:
        try:
            posts = r.json().get('data').get('children')
            for post in posts:
                print(post.get('data').get('title'))
        except:
            print("None")
