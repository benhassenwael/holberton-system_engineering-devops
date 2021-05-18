#!/usr/bin/python3
"""Function to recursively GET all the hot posts of a give subreddit"""
from requests import get, exceptions


def recurse(subreddit, hot_posts=[], after=None):
    """Use GET request to find the top 10 hot posts in `subreddit`"""
    try:
        r = get("https://www.reddit.com/r/{}/hot.json".format(subreddit),
                params={"after": after},
                headers={"User-Agent": "python:holberton project by 2244"},
                allow_redirects=False)
        r.raise_for_status()
    except exceptions.RequestException as e:
        return None
    else:
        try:
            posts = r.json().get('data').get('children')
            for post in posts:
                hot_posts.append(post.get('data').get('title'))
            after = r.json().get('data').get('after')
            if after is None:
                return hot_posts
            else:
                return recurse(subreddit, hot_posts, after=after)
        except Exception as e:
            return None
